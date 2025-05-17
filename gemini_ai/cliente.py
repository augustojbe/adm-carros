from google import genai

def get_car_ai_bio(model, brand, year):
  api_key = 'AIzaSyDpkdddpAogo5fce4JcLOfyDu0AHpfKtDk'
  prompt = f'(Cri uma descrição tecnica de venda para o caro {model} {brand} {year}, com no maximo 250 caracteres. Desteque pontos fortes como desempenho ou economia.)'
  client = genai.Client(api_key=api_key)
  
  response = client.models.generate_content(
    model="gemini-2.0-flash", contents=[prompt]
  )
  return response.text
  