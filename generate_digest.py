import openai
from config import XAI_API_KEY

openai.api_key = XAI_API_KEY

def generate_digest(letter):
    prompt = f"""
请根据以下FDA警告信内容生成中文简报，结构包括：
1. 概述（发出时间、对象企业、主要违规问题）；
2. 详细分析（具体违规事项、法规依据、潜在风险）；
3. 整改建议（针对违规事项提出具体解决方案）；
4. 总结（问题根因、行业启示）。

警告信内容如下：
{letter}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message["content"]
