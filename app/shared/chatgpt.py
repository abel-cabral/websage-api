import os
import json
import mongodb
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
  organization=os.getenv('ORGANIZATION'),
  project=os.getenv('PROJECT_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

def get_chatgpt_response(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7)
    return response



def classificarTagsGerais():
    return


# Exemplo de uso
messages = [
    {"role": "system", "content": "Receba um texto extraído de uma página HTML usando `document.body.innerText`, faça um resumo em até duas linhas (máximo 160 caracteres) e forneça três tags que representem os principais tópicos do texto. A resposta deve ser unicamente no formato JSON com as seguintes propriedades: mensagem (resumo), tag1 (primeira tag), tag2 (segunda tag) e tag3 (terceira tag), sem mais nenhum texto adicional."},
    {"role": "user", "content": 'Home Análises Artigos Notícias Produtos Ofertas Comparar Produtos Fórum Vídeos Hardware Games Microsoft Marcas Downloads Internet Periféricos Segurança Software Tutorial Variedades Tipos de Produtos Tipos de Ofertas Home Games REPORTAR ERRO MANEQUINS E HORRORES Silent Hill 2 Remake chega em outubro para PC e PS5 Após State of Play, Bloober Team e Konami apresentaram trailer de 13 minutos com muitos detalhes da exploração e gameplay de Silent Hill 2 Remake Luiz Schmidt 31/05/2024 07:57 4 COMPARTILHAR NO WHATSAPP Créditos: Bloober Team/Divulgação Durante o State of Play, da última quinta-feira (30), a Sony divulgou um novo trailer de Silent Hill 2 Remake. O jogo feito pela Bloober Team e publicado pela Konami vai chegar ao PS5 e PC no dia 8 de outubro de 2024. Jogadores compram menos jogos para PS5, mas gastam mais Helldivers 2 bane 20 mil jogadores da Rússia e Bielorrússia Sony vê aumento da popularidade do PS Plus O game é o remake de um grande clássico do gênero do horror, tendo a difícil missão de agradar os fãs do original e novos jogadores. Será que a Bloober Team conseguirá fazer o que a Capcom fez com os remakes de Resident Evil 2 e Resident Evil 4? Os trailers possuem restrição de idade, por isso será necessário assisti-los diretamente no YouTube. O primeiro trailer de Silent Hill 2 Remake mostra um pouco da ambientação do título e também a personagem Angela Orosco, figura central da trama. CRÉDITOS: Bloober Team Além disso, também vemos um pouco dos clássicos manequins do hospital, rastejando por todos os lados e atacando o jogador. Curiosamente, logo após a apresentação, a Bloober Team e a Konami se juntaram em uma livestream especial onde mostraram a fundo como ficou o gameplay de Silent Hill 2 Remake. Silent Hill 2 Remake recebeu novo trailer de gameplay após apresentação da Sony O Produtor da Konami, Motoi Okamoto, destacou que os 12 minutos de gameplay da nova transmissão de Silent Hill 2 Remake mostram um pouco mais da exploração do hospital e cidade. Com o vídeo é possível ver como ficou a movimentação do protagonista, a exploração das áreas e também os combates. Os 13 minutos de gameplay que revelamos durante a transmissão de Silent Hill 2 mostram a exploração da cidade e do hospital para que os jogadores entendam melhor como será o gameplay. Motoi Okamoto – Konami CRÉDITOS Bloober Team De acordo com Okamoto, o remake de Silent Hill 2 respeita o original. “Para satisfazer expectativas tão altas, dedicamos muito tempo para aprimorar o jogo e decidimos com cuidado quando seria possível lançá-lo com confiança. Este jogo é um remake que respeita o original“. Ainda durante o State of Play, a Sony também revelou trailers de Astro Bot, Concord, Monster Hunter Wilds, God of War Ragnarök no PC, Where Winds Meet, Infinity Nikki e muito mais. Com uma apresentação diversa, a Sony tentou mostrar diferentes jogos que devem chegar ao console nos anos de 2024 e 2025. Silent Hill 2 Remake chega no dia 8 de outubro no PlayStation 5 e PC! Jogo busca agradar fãs do clássico do gênero de horror e também atrair novos fãs. CONTEÚDO RELACIONADO O ASTRO VOLTOU! Astro Bot chega em setembro com 80 fases e muitas referências Fonte: PlayStation Blog Categorias GAMES NOTÍCIAS PC GAMES PLAYSTATION Tags BLOOBER TEAM GAMES KONAMI SILENT HILL 2 SILENT HILL 2 REMAKE Participe do grupo de ofertas do Adrenaline Confira as principais ofertas de hardware, componentes e outros eletrônicos que encontramos pela internet. Placa de vídeo, placa-mãe, memória RAM e tudo que você precisa para montar o seu PC. Ao participar do nosso grupo, você recebe promoções diariamente e tem acesso antecipado a cupons de desconto. ENTRE NO GRUPO E APROVEITE AS PROMOÇÕES MAIS LIDAS Hoje Semana Mês Ano 1 25 AINDA BEM ATRASADA Rússia desenvolve litografia própria que chega com 30 anos de atraso 2 DECISÃO SURPREENDEU AliExpress se posiciona contra taxação de compras abaixo de US$ 50 3 INFÂNCIA DESTRUÍDA Gamer encontra PS2 lacrado há 20 anos que pais esqueceram de dar 4 DESCONTOS ATÉ 12 DE JUNHO Assinatura da PS Plus está com desconto de até 30% no Days of Play 5 COMUNIDADE SE ORGANIZA Jogadores de League of Legends boicotarão novas skins VEJA TAMBÉM FINAL FELIZ Carregamento de R$ 2 milhões do Playdate é encontrado em restaurante ANÚNCIO COMPLETO NA COMPUTEX Zotac vai lançar PC portátil com AMD Ryzen 7 8840U e tela de 120Hz MESMO NO SINGLE PLAYER God of War Ragnarök e outros jogos da Sony vão exigir PSN no PC O ASTRO VOLTOU! Astro Bot chega em setembro com 80 fases e muitas referências OFERTAS DIVERSOS Mousepad Adrenaline, Kumori Deskma, Speed A PARTIR DE R$ 129 ,90 VÍDEO GAMES Controle DualSense, PS5, Sony, Midnight Black A PARTIR DE R$ 312 ,46 GAMES A Ascensão do Ronin, Mídia Física, PS5 A PARTIR DE R$ 209 ,92 VÍDEO GAMES PS5 Slim + 2 Jogos, Com Leitor de Discos, Branco A PARTIR DE R$ 3.460 ,52 TUDO SOBRE GAMES 1 OUTRO HERO SHOOTER Concord é o novo FPS da Sony e chega em agosto para PC e PS5 0 MAIS MONSTRINHOS Monster Hunter Wilds ganha novo trailer em State of Play 4 PRÊMIOS PARA A AUDIÊNCIA Ubisoft Forward: jogos que estarão no evento e recompensas para jogadores 0 ATÉ 12 DE JUNHO Jogos da franquia Monster Hunter em oferta na Steam com até 75% de desconto 59 RUMORES CONFIRMADOS God of War Ragnarök é confirmado para PC 0 GRANDES LANÇAMENTOS Principais lançamentos de jogos em junho de 2024 para PC, PlayStation, Xbox e Switch 2 DOIS LADOS DIFERENTES Jogadores compram menos jogos para PS5, mas gastam mais 0 ATÉ 13 DE JUNHO Jogos para PC em oferta por menos de R$ 50 na Epic Games Store - Mega Promoção CONTEÚDOS Análises Artigos Notícias Downloads EDITORIAS Games PC Games Playstation Xbox Nintendo e-Sport Variedades Tutorial Hardware AMD Internet Notebook NVIDIA Segurança Periféricos Intel VÍDEOS Gameplay Lives Montando PCs PC Baratinho PC da Crise Hardware Placas de Vídeo Processadores OFERTAS Processadores Monitores Placas-Mãe SSDS Acessórios Games Memórias Periféricos PRODUTOS Processador Monitor Computador Notebook Memórias Games SSD e HD Segurança Acessório Áudio Cooler Gabinete Outros Mouse Placa-mãe Placa de Vídeo PÁGINAS INSTITUCIONAIS Quem Somos Equipe Publicidade Fale Conosco Condições de Uso Política de Privacidade Adrenaline © 2024 Todos os direitos reservados.'}
]
response = get_chatgpt_response(messages)
mongodb.collection().insert_one(json.loads(response.choices[0].message.content))

print(response.choices[0].message.content)