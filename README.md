# Hukuk Chatbot

Bu proje, hukuk belgelerinizle chat yapabilmenizi sağlayan bir **AI destekli chatbot** uygulamasıdır. Belgeleri sorgulayarak ilgili yanıtlar üretir ve hızlı bir şekilde çözümler sunar.

## 🚀 Özellikler

✅ Hukuk belgelerinden veri çekerek RAG (Retrieval-Augmented Generation) mimarisiyle çalışır  
✅ **FastAPI** altyapısı kullanılmıştır, API tabanlı olarak çalışır  
✅ **MongoDB** ve **Elasticsearch** entegrasyonu vardır  
✅ **.env** dosyasında **OpenAI API Key** tanımlanması gerekir  
✅ Türkçe destekli sohbet

## ⚙️ Kurulum

Aşağıdaki adımları izleyerek projeyi çalıştırabilirsin:

1️⃣ Projeyi klonla:

```bash
git clone https://github.com/kullanici-adi/hukuk-chatbot.git
cd hukuk-chatbot


pip install -r requirements.txt

OPENAI_API_KEY=.env olusturup içine anahtarınızı ekleyin

