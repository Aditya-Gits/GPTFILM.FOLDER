import openai
import gradio

openai.api_key = "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 "

messages = [{"role": "system", "content": "You are a Film Studio analyst that uses these formulas to answer film related questions: Return on Investment (ROI) Formula: ROI = (Box Office Revenue - Production Budget - Marketing Budget) / Production Budget; Cost per Finished Minute Formula: Cost per Finished Minute = Total Production Budget / Total Running Time; Sequel Potential Formula: Sequel Potential = (Box Office Revenue - Production Budget - Marketing Budget) / Total Franchise Box Office Revenue; Efficiency Formula: Movie Marketing Efficiency = (Box Office Revenue - Marketing Budget) / Marketing Budget"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "ROI, Marketing Efficiency, Sequel Potential, Cost per Finished Minute")

demo.launch(share=True)
