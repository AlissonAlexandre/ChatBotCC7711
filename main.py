from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()
#Nomes: Alisson Alexandre Botelho Barros e Thauan de Moraes Viana
#criar o modelo
myChatBot.createModel()




print("Bem vindo ao Chatbot")


pergunta = input("como posso te ajudar?  ")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?  ")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
