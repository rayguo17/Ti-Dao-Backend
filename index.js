const { OpenAI } = require("langchain/llms/openai");

require("dotenv").config();
open_ai_api_key = process.env.OPEN_AI_API_KEY;

const model = new OpenAI({
    openAIApiKey: open_ai_api_key,
    modelName: "gpt-3.5-turbo",
    temperature: 0.9,
});

const res = model.call("What is the meaning of life?")
res.then((res) => { console.log(res) })