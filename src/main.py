from agent import SimpleAgent


def main():
    print("AI Agent Workflow Assistant")
    print("请输入一个任务目标，Agent 会生成任务拆解和执行建议。")
    print("示例：帮我设计一个用于整理学习资料的 AI Agent 工作流")
    print("-" * 60)

    task = input("请输入任务目标：").strip()
    if not task:
        task = "帮我设计一个用于整理学习资料的 AI Agent 工作流"

    agent = SimpleAgent()
    result = agent.run(task)

    print("\n" + "=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()

