# graph_image.py : LangGraph 그래프의 모양(노드 흐름)을 그림 파일로 저장하는 도우미
# ── 전체 흐름 ──────────────────────────────────────────────
# ① app.get_graph() 로 그래프의 노드 · 엣지 정보를 꺼내요
# ② Mermaid(글자로 그림을 그리는 언어)로 바꾼 뒤, mermaid.ink 사이트가 PNG 그림으로 그려 줘요 (인터넷 필요)
# ③ 인터넷이 안 되면 그림 대신 Mermaid 글자를 .mmd 파일로 저장해요
#    → https://mermaid.live 에 그 글자를 붙여 넣으면 같은 그림이 보여요
# 그림 읽는 법: 맨 위 __start__ 에서 출발 → 화살표를 따라 노드 실행 → __end__ 에서 끝
#              실선 화살표 = 늘 가는 길, 점선 화살표 = 갈림길(조건에 따라 하나만 가는 길)
# ────────────────────────────────────────────────────────
import os                                         # 폴더 만들기 · 경로 합치기


def save_graph(app, file_name):
    """compile 한 그래프(app)의 모양을 images 폴더에 그림으로 저장해요."""
    os.makedirs("images", exist_ok=True)          # images 폴더가 없으면 만들기 (있으면 그대로)
    path = os.path.join("images", file_name)      # 예: images/ex06_graph.png
    graph = app.get_graph()                       # ① 노드 · 엣지 정보
    try:
        png = graph.draw_mermaid_png()            # ② 그림(PNG) 데이터 받기
        with open(path, "wb") as file:            # "wb" = 그림 같은 바이트 파일로 쓰기
            file.write(png)
        print("그래프 그림 저장:", path)
    except Exception:                             # ③ 인터넷 문제 등으로 그림을 못 받으면
        mmd_path = path.replace(".png", ".mmd")   # 확장자만 .mmd 로
        with open(mmd_path, "w", encoding="utf-8") as file:
            file.write(graph.draw_mermaid())      # 그림 대신 Mermaid 글자로 저장
        print("그림을 받지 못해 글자로 저장:", mmd_path, "→ https://mermaid.live 에 붙여 넣어 보세요")
