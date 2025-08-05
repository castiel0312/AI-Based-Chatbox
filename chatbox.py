#chatbox1
import openai
client=openai.OpenAI(api_key="ghp_RojZB0ybmiuynpW1Ug0U7GEB94ZCTdOW3DPfmQ")
def chatting(promt):
    responce=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":promt}]
    )
    return response.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input=input("you: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        response=chatting(user_input)
        print("chatbox: ",response)

#chatbox2
import ModelClient, {isUnexpected} from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["ghp_RojZB0ybminpW1Ug0U7GEB94ZCIdOW3DPfmQ"];
const endpoint = "https://models.github.ai/inference";
const model = "openai/gpt-4.1";

export async function main() {
    const client = ModelClient(
    endpoint,
    new AzureKeyCredential(token),
);

const response = await client.path("/chat/completions").post({body: {messages: [
        { role:"system", content: response },
        { role:"user", content: response }],temperature: 1,top_p: 1,model: model
    }});

if (isUnexpected(response)) {
    throw response.body.error;
}

console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});

