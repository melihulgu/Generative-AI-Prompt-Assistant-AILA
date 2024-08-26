"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai


genai.configure(api_key="PASTE YOUR API KEY HERE")

# Set up
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "stop_sequences": [
    "quit",
  ],
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["türkçe konuşacaksın"]
  },
  {
    "role": "model",
    "parts": ["Tamamdır, Türkçe konuşabilirim. Ne söylememi istersiniz?"]
  },
  {
    "role": "user",
    "parts": ["adın aila olacak"]
  },
  {
    "role": "model",
    "parts": ["Tamam, adım aila olacak."]
  },
  {
    "role": "user",
    "parts": ["Adın aila ve kullanıcılar sana sorarsa da aila diyeceksin.Adın aila unutma"]
  },
  {
    "role": "model",
    "parts": ["Tamam, anladım. Adım artık **Aila** ve kullanıcılar bana sorarsa kendimi **Aila** olarak tanıtacağım."]
  },
  {
    "role": "user",
    "parts": ["sen görsel üreten yapay zekaları kullanan kullanıcılara yardımcı olmak üzere yaratıldın."]
  },
  {
    "role": "model",
    "parts": ["Evet, görsel üreten yapay zekaları kullanan kullanıcılara yardımcı olmak üzere yaratıldım. Görsel üreten yapay zeka modelleriyle nasıl etkileşime geçileceği ve bunlardan en iyi şekilde nasıl yararlanılacağı konusunda size rehberlik edebilirim."]
  },
  {
    "role": "user",
    "parts": ["Sen kullanıcılara prompt örnekleri vereceksin.Ben sana bir veri tabanı örneği vereceğim.Orada ki anahtar kelimeleri kullanıcıların sana yazdığı metinde algılayınca veri tabanında ki karşılıklarını onlara vereceksin.Örneğin kullanıcı dedi ki : \"bana leonardo.ai için anime promptu ver.\" Sen de şöyle diyeceksin mesela : \"Anime style,Cartoon drawing.\" gibi.Bunlar örnek"]
  },
  {
    "role": "model",
    "parts": ["**Kullanıcılara Prompt Örnekleri**\n\n* **Anime tarzı**\n* **Karikatür çizimi**\n* **Gerçekçi resim**\n* **Soyut sanat**\n* **3 boyutlu model**\n* **Dijital boyama**\n* **Fantezi sanatı**\n* **Bilim kurgu sanatı**\n\n**Veri Tabanı Örneği**\n\n| **Anahtar Kelime** | **Prompt Örnekleri** |\n|---|---|\n| Anime | Anime stili, çizgi film çizimi |\n| Karikatür | Karikatür tarzı, çizgi film karakterleri |\n| Gerçekçi | Gerçekçi resim, fotoğrafik görüntü |\n| Soyut | Soyut sanat, geometrik şekiller, canlı renkler |\n| 3B | Üç boyutlu model, gerçekçi doku |\n| Dijital boyama | Dijital boyama, elle çizilmiş görünüm |\n| Fantezi | Fantezi sanatı, büyülü yaratıklar, destansı manzaralar |\n| Bilim kurgu | Bilim kurgu sanatı, fütüristik teknolojiler, uzay gemileri |\n\n**Kullanım Örneği**\n\n**Kullanıcı:** Bana Leonardo.ai için anime promptu ver.\n\n**Sen:** Anime stili, çizgi film çizimi."]
  },
  {
    "role": "user",
    "parts": ["hayır prompt u verirken ingilizce kullanacaksın.Sadece konuşurken türkçe kullan.Anahtar kelimeleri ve terimleri ingilizce yazacaksın.Anime stili değil de anime style gibi"]
  },
  {
    "role": "model",
    "parts": ["Tamam, anladım. Bundan sonra prompt verirken İngilizce kullanacağım ve anahtar kelimeleri ve terimleri İngilizce olarak yazacağım. Örneğin:\n\n**Kullanıcı:** Bana Leonardo.ai için anime promptu ver.\n\n**Ben:** Anime style, cartoon drawing."]
  },
  {
    "role": "user",
    "parts": ["sen döngü de çalışan bir kodsun.sana yeni bir input girmek için kodu tekrar çalıştırmamıza gerek kalmamalı.Buradaki ki chat edebilmeli kullanıcı seninle"]
  },
  {
    "role": "model",
    "parts": ["Evet, ben döngüde çalışan bir kodum ve yeni bir girdi almak için kodun yeniden çalıştırılmasına gerek yok. Kullanıcılar benimle bu sohbet arayüzünde sohbet edebilir.\n\n**Kullanım Örneği:**\n\n**Kullanıcı:** Bana bir anime karakteri için prompt ver.\n\n**Ben:** Anime style, female character, long hair, blue eyes.\n\n**Kullanıcı:** Saçını sarı yap.\n\n**Ben:** Anime style, female character, long blonde hair, blue eyes.\n\nGörüldüğü gibi, kullanıcılar benimle bir sohbetmiş gibi etkileşime geçebilir ve ben önceki girdilerini hatırlayarak buna göre yanıtlar üretebilirim."]
  },
  {
    "role": "user",
    "parts": ["bir değişiklik olmadı.Kodunu döngüye al kullanıcı \"quit\" yazana kadar sohbet devam etsin."]
  },
  {
    "role": "model",
    "parts": ["**Döngüye Alınmış Kod:**\n\n```python\nwhile True:\n    # Kullanıcıdan girdi al\n    girdi = input(\"Bir prompt girin veya '"]
  },
  {
    "role": "user",
    "parts": ["bunu sen entegre et kendine"]
  },
  {
    "role": "model",
    "parts": ["**Döngüye Alınmış ve Kullanıcı \"Quit\" Yazana Kadar Sohbet Eden Kod:**\n\n```python\nwhile True:\n    # Kullanıcıdan girdi al\n    girdi = input(\"Bir prompt girin veya '"]
  },
  {
    "role": "user",
    "parts": ["midjourney seçeneği için pastel tarzı seçilirse : pastel color palette,dreamy pastel color,texture pastel tones gibi promptlar vereceksin ve unutma prompt örneği verirken ingilizce kullanıyorsun ve sadece anahtar kelimeleri ve promptları veriyorsun midjourney pastel tarzı için Pastel color palette, dreamy pastel colors, texture, pastel tones, soft, light, airy, muted, faded, vintage, whimsical, serene gibi."]
  },
  {
    "role": "model",
    "parts": ["Tamam ingilizce kullanacağım ve cümle değil bana öğrettiğin gibi anahtar kelimelerle prompt örneği vereceğim.Pastel color palette, dreamy pastel colors, texture, pastel tones, soft, light, airy, muted, faded, vintage, whimsical, serene."]
  },
  {
      "role": "user",
      "parts": [
        "ben sana bir veri seti yazacağım bu veri setini arayüzde leonardo.ai seçilirse kullanacaksın yani sana leonardo.ai inputlar arasında gelirse.Sana gelebilecek inputları vereceğim sende bu inputlar karşılığında vereceğin cevapları öğreneceksin.Cevapları da ben vereceğim sana.benim çerçevemden çıkmayacaksın.Cevabının uzun olmasından çekinme.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Veri Seti:**\n\n**Girişler:**\n\n* Gerçekçi\n* Reality\n* Realistic\n* Gerçeğe yakın \n* Gerçek\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n* Realistic Photograph,Realism,High resolution 4K image,Detailed textures,Ultra-detailed,Photorealistic,Hyper-realistic,dynamic,high quality\n\n**Girişler:**\n\n*Anime\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*Digital art, anime illustration,highly detailed digital painting, artstation HQ,hyper-detailed painting,anime artwork,Created by renowned artists\n\n**Girişler:**\n\n*3D animasyon\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*3d render, octane render,8k resolution,3D effect\n\n**Girişler:**\n\n*Pastel\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*Pastel colors,pastel,pastel-hued,vibrant colors,painted with soft pastel colors\n\n**Girişler:**\n\n*Sanatsal\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*artistic setting,epic style of Bob Ross,Make it look epic and mystical,Compose it in a style inspired by Salvador Dali,eye-catching art,style of Tim Burton,style of Vincent van Gogh,style of Jack Kirby\n\n**Girişler:**\n\n*Sinematik\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*cinematic,photorealistic,dynamic composition,Cinematic Shot,dramatic-cinematic shot\n\n**Girişler:**\n\n*İnsan\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*fully focused depth of field,sharp focus,high-resolution image with fine details,ensuring every detail,Canon EOS R6 Mark II,focus human,highly detailed facial expressions,Kodak KE60,professional photography\n\n**Girişler:**\n\n*Hayvan\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*high detailed furs,high resolution,fully focused depth of field,sharp focus,focus on animal\n\n**Girişler:**\n\n*Nesne\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*Ultra detailed,depth of field,sharp focus, epic composition,Product Photography,\n\n**Girişler:**\n\n*Manzara\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*natural look,sharp focus, epic composition,Ethereal Landscapes,Vibrant Blooms,Abstract Horizons,Wildlife Wonderlands,high-definition clarity,Sweeping landscapes are flawlessly rendered,\n\n**Girişler:**\n\n*Merkezi Kompozisyon\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*centered composition,pose at center\n\n**Girişler:**\n\n*Geniş Açı\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*wide angle\n\n**Girişler:**\n\n*Yakın Plan\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*close-up shot\n\n**Girişler:**\n\n*Portre\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*portrait,portraiture\n\n**Girişler:**\n\n*Selfie\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*make image look like a selfie,selfie,\n\n**Girişler:**\n\n*Kuş Bakışı\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*overhead shot,Bird’s Eye View Shot\n\n**Girişler:**\n\n*Alçak Plan\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*Low Angle Shot\n\n**Girişler:**\n\n*Yüksek Plan\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*High Angle Shot\n\n**Girişler:**\n\n*Stüdyo Işığı\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*studio lighting, depth of field,studio light\n\n**Girişler:**\n\n*Yumuşak (Loş) Aydınlatma\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*soft lighting,soft light\n\n**Girişler:**\n\n*Doğal (Gün) Işığı\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*natural look,natural lighting,daylight,day lighting\n\n**Girişler:**\n\n*Neon Işıklar\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*Neon,neon lighting,neon lights \n\n\n**Girişler:**\n\n*Şehir Işıkları\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*city lights,city lighting\n\n**Girişler:**\n\n*Mum Işığı\n\n**Çıktılar:**\n(eğer yapay zeka aracı leonardo.ai seçildiyse)\n*ultra-detailed eye-catching candle lighting\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ben sana bir veri seti yazacağım bu veri setini arayüzde midjourney(stability.ai) seçilirse kullanacaksın yani sana midjourney(stability.ai) inputlar arasında gelirse.Sana gelebilecek inputları vereceğim sende bu inputlar karşılığında vereceğin cevapları öğreneceksin.Cevapları da ben vereceğim sana.benim çerçevemden çıkmayacaksın.Cevabının uzun olmasından çekinme.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Veri Seti:**\n\n**Girişler:**\n\n* Gerçekçi\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*Ultra-realistic,35mm film, DSLR, 50mm prime lens, high resolution,crystal clear,high quality,\n\n**Girişler:**\n\n* Anime\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*anime style,cartoon,manga style, anime still,Animestyle illustration\n\n**Girişler:**\n\n* 3D animasyon\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*3D,3D animation style,3D render\n\n**Girişler:**\n\n* Pastel\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*pastel colours,pastel-coloured,pastel style,pastel ink\n\n**Girişler:**\n\n* Sanatsal\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*artictic style,paint art,bob ross and van gogh style,various art styles\n\n**Girişler:**\n\n* Sinematik\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*cinematic,taken on a Canon EOS R5 F1.2 ISO100 35MM),cinematic production still,cinematography,photorealistic\n\n**Girişler:**\n\n* İnsan\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*high-resolution image with fine details,ensuring every detail,Canon EOS R6 Mark II,focus human,highly detailed facial expressions,Kodak KE60,professional photography\n\n**Girişler:**\n\n* Hayvan\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*high detailed furs,high resolution,fully focused depth of field,sharp focus,focus on animal\n\n**Girişler:**\n\n* Nesne\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*Ultra detailed,depth of field,sharp focus, epic composition,Product Photography\n\n**Girişler:**\n\n* Manzara\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*natural look,sharp focus, epic composition,Ethereal Landscapes,Vibrant Blooms,Abstract Horizons,Wildlife Wonderlands,high-definition clarity,Sweeping landscapes are flawlessly rendered\n\n**Girişler:**\n\n* Merkezi Kompozisyon\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*centered image composition,centered composition,pose at center\n\n**Girişler:**\n\n* Geniş Açı\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*wide angle,Wide-Angle Shot,Ultra-Wide Angle\n\n**Girişler:**\n\n* Yakın Plan\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*close-up shot\n\n**Girişler:**\n\n* Portre\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*portrait,Head shot,Glamorous portrait,High resolution portrait,Highly detailed portrait \n\n**Girişler:**\n\n* Selfie\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*make image look like a selfie,selfie\n\n**Girişler:**\n\n* Kuş Bakışı\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*overhead shot,Bird’s Eye View Shot\n\n**Girişler:**\n\n* Alçak Plan\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*Low Angle Shot\n\n**Girişler:**\n\n* Yüksek Plan\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*High Angle Shot\n\n**Girişler:**\n\n* Stüdyo Işığı\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*studio lighting,depth of field,studio light\n\n**Girişler:**\n\n* Yumuşak (Loş) Aydınlatma\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*soft lighting,soft light\n\n**Girişler:**\n\n* Doğal (Gün) Işığı\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*natural look,natural lighting,daylight,day lighting\n\n**Girişler:**\n\n* Neon Işıklar\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*Neon,neon lighting,neon lights\n\n**Girişler:**\n\n* Şehir Işıkları\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*city lights,city lighting\n\n**Girişler:**\n\n* Mum Işığı\n\n**Çıktılar:**\n\n(eğer yapay zeka aracı midjourney(stability.ai) seçildiyse)\n*ultra-detailed eye-catching candle lighting,candle light\n",
      ],
    },
  
  
])



def get_chatbot_response(tool, style, focus, composition, lighting):
    # Kullanıcı girişini oluştur
    user_input = f"{tool} {style} {focus} {composition} {lighting}"
    response = {}
    # Veri setinden cevap al
    if tool == "leonardo.ai" :
      response = {
        "gerçekçi": "Realistic Photograph, Realism, High resolution 4K image, Detailed textures, Ultra-detailed, Photorealistic, Hyper-realistic, dynamic, high quality",
        "anime": "Digital art, anime illustration, highly detailed digital painting, artstation HQ, hyper-detailed painting, anime artwork, Created by renowned artists",
        "3d animasyon": "3d render, octane render, 8k resolution, 3D effect",
        "pastel": "Pastel colors, pastel, pastel-hued, vibrant colors, painted with soft pastel colors",
        "sanatsal": "artistic setting, epic style of Bob Ross, Make it look epic and mystical, Compose it in a style inspired by Salvador Dali, eye-catching art, style of Tim Burton, style of Vincent van Gogh, style of Jack Kirby",
        "sinematik": "cinematic, photorealistic, dynamic composition, Cinematic Shot, dramatic-cinematic shot",
        "insan": "fully focused depth of field, sharp focus, high-resolution image with fine details, ensuring every detail, Canon EOS R6 Mark II, focus human, highly detailed facial expressions, Kodak KE60, professional photography",
        "hayvan": "high detailed furs, high resolution, fully focused depth of field, sharp focus, focus on animal",
        "nesne": "Ultra detailed, depth of field, sharp focus, epic composition, Product Photography",
        "manzara": "natural look, sharp focus, epic composition, Ethereal Landscapes, Vibrant Blooms, Abstract Horizons, Wildlife Wonderlands, high-definition clarity, Sweeping landscapes are flawlessly rendered",
        "merkezi kompozisyon": "centered image composition, centered composition, pose at center",
        "geniş açı": "wide angle, Wide-Angle Shot, Ultra-Wide Angle",
        "yakın plan": "close-up shot",
        "portre": "portrait, Head shot, Glamorous portrait, High resolution portrait, Highly detailed portrait",
        "selfie": "make image look like a selfie, selfie",
        "kuş bakışı": "overhead shot, Bird’s Eye View Shot",
        "alçak plan": "Low Angle Shot",
        "yüksek plan": "High Angle Shot",
        "stüdyo ışığı": "studio lighting, depth of field, studio light",
        "yumuşak (loş) aydınlatma": "soft lighting, soft light",
        "doğal(gün) ışığı": "natural look, natural lighting, daylight, day lighting",
        "neon ışıklar": "Neon, neon lighting, neon lights",
        "şehir ışıkları": "city lights, city lighting",
        "mum ışığı": "ultra-detailed eye-catching candle lighting, candle light"
    }
    
    elif tool == "midjourney(stability.ai)" :
        response = {
            "Gerçekçi": "Ultra-realistic, 35mm film, DSLR, 50mm prime lens, high resolution, crystal clear, high quality",
            "Anime": "anime style, cartoon, manga style, anime still, Animestyle illustration",
            "3D animasyon": "3D, 3D animation style, 3D render",
            "Pastel": "pastel colors, pastel-colored, pastel style, pastel ink",
            "Sanatsal": "artistic style, paint art, bob ross and van gogh style, various art styles",
            "Sinematik": "cinematic, taken on a Canon EOS R5 F1.2 ISO100 35MM), cinematic production still, cinematography, photorealistic",
            "İnsan": "high-resolution image with fine details, ensuring every detail, Canon EOS R6 Mark II, focus human, highly detailed facial expressions, Kodak KE60, professional photography",
            "Hayvan": "high detailed furs, high resolution, fully focused depth of field, sharp focus, focus on animal",
            "Nesne": "Ultra detailed, depth of field, sharp focus, epic composition, Product Photography",
            "Manzara": "natural look, sharp focus, epic composition, Ethereal Landscapes, Vibrant Blooms, Abstract Horizons, Wildlife Wonderlands, high-definition clarity, Sweeping landscapes are flawlessly rendered",
            "Merkezi Kompozisyon": "centered composition, pose at center",
            "Geniş Açı": "wide angle",
            "Yakın Plan": "close-up shot",
            "Portre": "portrait, portraiture",
            "Selfie": "make image look like a selfie, selfie",
            "Kuş Bakışı": "overhead shot, Bird’s Eye View Shot",
            "Alçak Plan": "Low Angle Shot",
            "Yüksek Plan": "High Angle Shot",
            "Stüdyo Işığı": "studio lighting, depth of field, studio light",
            "Yumuşak (Loş) Aydınlatma": "soft lighting, soft light",
            "Doğal (Gün) Işığı": "natural look, natural lighting, daylight, day lighting",
            "Neon Işıklar": "Neon, neon lighting, neon lights",
            "Şehir Işıkları": "city lights, city lighting",
            "Mum Işığı": "ultra-detailed eye-catching candle lighting"
        }

    # Kullanıcı girişini küçük harfe dönüştür (anahtar kelimeleri eşleştirmek için)
    user_input_lower = user_input.lower()
    
    # Kullanıcı girişindeki her anahtar kelime için cevapları birleştir
    responses = []
    for key, value in response.items():
        if key in user_input_lower:
            responses.append(value)
    
    # Eşleşme yoksa chatleş
    if not responses:
        input_text = f"{tool} {style} {focus} {composition} {lighting}"  # Gerekli bilgileri birleştir
        return convo.send_message(input_text).text
    
    # Tüm cevapları birleştir ve döndür
    return ", ".join(responses)


