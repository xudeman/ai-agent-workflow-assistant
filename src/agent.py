from workflow import build_workflow


class SimpleAgent:
    """一个简单的 Agent 示例，用于展示任务理解、拆解和结果生成。"""

    def run(self, task: str) -> str:
        workflow = build_workflow(task)
        output = []
        output.append(f"任务目标：{task}")
        output.append("\nAgent 拆解结果：")

        for index, step in enumerate(workflow, start=1):
            output.append(f"{index}. {step}")

        output.append("\n结果建议：")
        output.append("- 将任务拆解结果保存为 Markdown 文档，方便复用。")
        output.append("- 如果任务涉及代码，可以进一步生成函数、测试用例和 README。")
        output.append("- 如果任务涉及资料整理，可以增加关键词提取和摘要生成环节。")
        output.append("- 后续可接入真实 LLM API，使 Agent 具备更强的理解和执行能力。")

        return "\n".join(output)
