
🚀 ERP Market – Modular Django ERP System

ERP Market — bu zamonaviy, “clean-design” ga ega, modul asosidagi ERP platforma bo‘lib, inventarizatsiya, sotuv, xarid, xarajatlar va foydalanuvchilar boshqaruvini yagona boshqaruv panelida birlashtiradi. Loyihada Django 5, Bootstrap 5 va Chart.js asosiy texnologiyalar sifatida ishlatilgan.

⸻

🌟 Platforma Imkoniyatlari

Modul	Asosiy imkoniyatlari
Dashboard	KPI’lar, kategoriya bo‘yicha pie-chart, oyma-oy daromad/xarajat
Inventarizatsiya	Mahsulotlar, kategoriyalar, omborlar, zaxira harakati
Sotuvlar	Mijozlar, sotuv buyurtmalari, inline mahsulotlar, foyda hisoblash
Xaridlar	Yetkazib beruvchilar, xarid buyurtmalari, avtomatik zaxira kiritish
Xarajatlar	Kategoriya va izoh bilan xarajatlarni kiritish
Foydalanuvchilar	Rollar: SuperAdmin · Admin · Staff (custom @role_required)
Demo data	1 ta buyruq bilan Faker orqali demo bazani to‘ldirish


⸻

🏗️ Texnologiyalar
	•	Python 3.13, Django 5.2
	•	SQLite (tezkor test uchun, istalgan DBMS’ga almashtirish mumkin)
	•	Bootstrap 5.3 — front-end va custom CSS
	•	Chart.js 4 — diagramma/diagrammalar
	•	django-widget-tweaks — shakl dizayni uchun
	•	Faker — demo/seeder data uchun

⸻

⚡ Tez start (Local)

# 1. Klon va papkaga kirish
git clone <repo-url> ERP_MARKET && cd ERP_MARKET

# 2. Virtual muhit yaratish
python -m venv venv && source venv/bin/activate

# 3. Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiya va admin user yaratish
python manage.py migrate
python manage.py createsuperuser

# 5. (ixtiyoriy) Demo data qo‘shish
python manage.py fake_demo --scale 40

# 6. Serverni ishga tushurish
python manage.py runserver

👉 Ochish: http://127.0.0.1:8000

⸻

🔑 Muhit sozlamalari

O‘zgaruvchi	Default / Qayerda	Izoh
DJANGO_SECRET_KEY	src/settings.py	Produktsiyaga almashtirilsin
DEBUG	True	Produktsiyada False
ALLOWED_HOSTS	[]	Hostlarni kiriting


⸻



🗂️ Loyihaning asosiy tuzilmasi

ERP_MARKET/
│
├── apps/                        # Barcha asosiy Django app'lar
│   ├── core/                    # Umumiy mikskinlar, helper, management commands
│   ├── dashboard/               # Bosh sahifa (dashboard), statistikalar va KPIs
│   ├── expenses/                # Xarajatlar va xarajat kategoriyalari
│   ├── inventory/               # Mahsulotlar, kategoriyalar, omborxonalar, zaxira harakati
│   ├── purchasing/              # Yetkazib beruvchilar va xarid buyurtmalari
│   ├── reports/                 # (Qo‘shimcha hisobotlar uchun)
│   ├── sales/                   # Mijozlar va sotuv buyurtmalari
│   └── users/                   # Foydalanuvchilar va rollar boshqaruvi
│
├── media/                       # Yuklangan fayllar (user avatar, product img, ...)
│   └── avatars/                 # Profil rasmlari va boshqa media fayllar
│
├── src/                         # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Bosh sozlamalar
│   ├── urls.py
│   └── wsgi.py
│
├── static/                      # Statik fayllar (CSS, JS, img, ...)
│   ├── css/
│   ├── icons/
│   └── js/
│
├── templates/                   # Jinja/Django HTML template’lar
│   ├── auth/                    # Login/register va user auth template’lari
│   ├── dashboard/
│   ├── expenses/
│   ├── inventory/
│   ├── partials/                # Qisman chaqiriladigan qismlar (modal, nav, ...)
│   ├── purchasing/
│   ├── sales/
│   ├── users/
│   └── base.html                # Bosh layout
│
├── venv/                        # Virtual environment (ignore qilinadi)
│
├── db.sqlite3                   # SQLite database (test/prototip uchun)
├── manage.py                    # Django project CLI
├── requirements.txt             # Barcha dependency’lar ro‘yxati (pip freeze)
└── README.MD                    # Loyihaga qisqacha ko‘rsatma/instruksiya


⸻

📊 Diagramma va grafiklar
	•	Chart.js — CDN orqali ulangan, hech qanday extra sozlash shart emas.
	•	Ma’lumotlar Django view’dan JSON ko‘rinishida uzatiladi.
	•	KPI’lar, kategoriyaviy sotuvlar va oyma-oy daromad/xarajatlar bir qarashda ko‘rinadi.

⸻

🎲 Demo (seed) ma’lumotlar yaratish

# Ehtiyot bo‘ling: mavjud bazani o‘chiradi!
rm db.sqlite3 && python manage.py migrate

# 10 ta demo obyekt uchun:
python manage.py fake_demo --scale 10

Demo ma’lumotlar: kategoriya, mahsulot, ombor, mijoz, yetkazib beruvchi, harakatlar, sotuv/xarid/xarajatlar.

⸻

📸 Ekranlar

Ekran tasvirlari uchun joy…
Dashboard, mahsulotlar, sotuv va xarajatlar oynasidan real skrinshotlar qo‘shing.

⸻

🧑‍💻 Xissa qo‘shish (Contributing)
	1.	Fork qiling, yangi branch oching
	2.	Kodni black . va isort . bilan format qiling
	3.	PR (pull request) ochishda nimalar o‘zgarganini qisqacha yozing

⸻

📄 Litsenziya

MIT (ochiq, istalgancha ishlatish mumkin)

⸻

Loyihani katta ishtiyoq va fidokorlik bilan, zamonaviy ERP uchun eng yaxshi tajribalar asosida tayyorlandi! 🇺🇿

⸻

Qisqacha
	•	Minimal va tez – 5 daqiqada localda ishga tushadi
	•	Har bir modulda CRUD (yaratish/o‘chirish/tahrirlash) imkoniyati bor
	•	Diagrammalar — real vaqt statistikasi
	•	SuperAdmin rollar va foydalanuvchilarni boshqaradi
	•	Faker seeder yordamida demo/test uchun to‘liq baza bir necha soniyada

⸻

