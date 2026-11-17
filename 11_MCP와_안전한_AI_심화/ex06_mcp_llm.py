# ex06_mcp_llm.py : LLM + MCP — LLM 이 MCP 서버의 도구를 골라 쓰게 하기
import asyncio
import json
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from llm import MODEL, client

SERVER = StdioServerParameters(command=sys.executable, args=["mcp_server.py"])


def text_of(result):
    """MCP 도구 결과(여러 조각일 수 있어요)를 글자 하나로 합쳐요."""
    return ", ".join(c.text for c in result.content)


async def main(questions):
    async with stdio_client(SERVER) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # ① MCP 도구 목록 → LLM 이 이해하는 tools 모양으로 바꾸기
            mcp_tools = (await session.list_tools()).tools
            tools = [{"type": "function", "function": {
                "name": t.name, "description": t.description, "parameters": t.input_schema}} for t in mcp_tools]

            for question in questions:                # 같은 서버에 질문을 차례로 (메모가 이어져요)
                print("Q:", question)
                messages = [{"role": "user", "content": question}]
                msg = client().chat.completions.create(model=MODEL, messages=messages, tools=tools).choices[0].message
                messages.append(msg)
                # ② LLM 이 고른 도구를 MCP 서버에서 실행하고 결과를 대화에 붙이기
                for call in msg.tool_calls or []:
                    args = json.loads(call.function.arguments or "{}")
                    result = text_of(await session.call_tool(call.function.name, args))
                    print(f"   도구 실행: {call.function.name}({args}) → {result}")
                    messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
                # ③ 도구 결과를 보고 최종 답 만들기
                final = client().chat.completions.create(model=MODEL, messages=messages, tools=tools)
                print("답:", final.choices[0].message.content)


asyncio.run(main(["오늘 날짜가 뭐야?", "'팀 회의 3시' 를 메모해 줘.", "지금 메모 목록 보여 줘."]))
