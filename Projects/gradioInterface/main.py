import gradio as gr
import matplotlib as plt
import numpy as np


def hello(name_input, marks):
    if marks >= 93:
        return f"Welcome! Dear  {name_input}, you got {marks} Result = Pass "
    return f"Welcome! Dear  {name_input}, you got {marks}, Result = Fail "


demo = gr.Interface(fn=hello, inputs=["text", "number"], outputs="label")
demo.launch(share=True)

