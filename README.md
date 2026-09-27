> **Final Project — Hacktiv8 Indonesia | AI & LLM Training**

Programming AI Assistant adalah chatbot berbasis **Python** dan **Google Gemini API** yang dirancang khusus untuk membantu menjawab pertanyaan seputar **Programming, IT, Software Engineering, dan Computer Science**.

Project ini dibuat sebagai bagian dari **Final Project** yang diberikan oleh tim **Hacktiv8 Indonesia** dalam pelatihan **AI dan LLM**, yang berlangsung pada **21–25 September 2026**.

---

## 📌 Project Overview

Tujuan utama project ini adalah membuat sebuah chatbot sederhana yang dapat berinteraksi dengan pengguna menggunakan Large Language Model (LLM), tetapi dengan **domain yang dibatasi**.

Berbeda dengan chatbot general-purpose, chatbot ini difokuskan pada topik:

* 💻 Programming
* 🖥️ Information Technology
* 🧑‍💻 Software Engineering
* 🧠 Computer Science
* 🌐 Web Development
* 📱 Mobile Development
* 🐳 Docker & DevOps
* ☁️ Cloud Computing
* 🔐 Cybersecurity
* 🗄️ Database
* 🌐 Networking
* 🐧 Linux
* 🪟 Windows
* 🔧 Developer Tools
* 📚 Algorithms & Data Structures

Chatbot akan menolak pertanyaan yang berada di luar domain tersebut.

### 🌐 No Internet Search

Chatbot ini **tidak menggunakan internet search atau web browsing**.

Gemini hanya menjawab berdasarkan:

1. Pengetahuan yang dimiliki oleh model.
2. Konteks percakapan yang diberikan oleh pengguna.

Project ini tidak menggunakan Google Search Grounding, web crawler, atau search engine API.

---

# ✨ Features

* 🤖 Powered by **Google Gemini**
* 💬 Interactive chatbot interface
* 🖥️ Desktop GUI menggunakan **CustomTkinter**
* 🔑 Input Gemini API Key melalui aplikasi
* 🧑‍💻 Fokus pada Programming & IT
* 🚫 Menolak pertanyaan di luar domain
* 🌐 Tidak melakukan internet search
* 🧵 Menggunakan threading agar UI tidak freeze ketika menunggu response
* 📦 Struktur kode sederhana dan mudah dikembangkan

---

# 🛠️ Technologies

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| Python            | Main programming language        |
| Google Gemini API | Large Language Model             |
| `google-genai`    | Official Google GenAI Python SDK |
| CustomTkinter     | Desktop graphical user interface |
| Threading         | Menjaga UI tetap responsif       |

---

# 📂 Project Structure

```text
programming-chatbot/
│
├── main.py
├── ui.py
├── ai.py
├── requirements.txt
└── README.md
```

### `main.py`

Entry point aplikasi.

File ini bertugas menjalankan aplikasi chatbot.

```python
from ui import ChatbotUI


if __name__ == "__main__":
    app = ChatbotUI()
    app.run()
```

---

### `ui.py`

Berisi seluruh komponen **Graphical User Interface (GUI)**.

Tanggung jawabnya antara lain:

* Membuat window aplikasi.
* Membuat input API Key.
* Membuat chat area.
* Membuat input message.
* Menangani tombol `Send`.
* Menampilkan response dari Gemini.
* Mengatur status koneksi.
* Menjalankan request Gemini pada thread terpisah.

Secara sederhana:

```text
User
 │
 ├── API Key
 │
 ├── Message
 │
 ▼
UI (CustomTkinter)
 │
 ▼
ProgrammingAI
```

Threading digunakan agar proses request ke Gemini tidak menghentikan event loop GUI.

Tanpa threading, UI berpotensi terlihat freeze selama aplikasi menunggu response dari API.

---

### `ai.py`

File ini merupakan bagian **AI Engine** dari aplikasi.

Di dalamnya terdapat class:

```python
class ProgrammingAI:
```

Class tersebut bertanggung jawab untuk:

* Membuat Gemini client.
* Membuat conversation/chat session.
* Menentukan system instruction.
* Mengirim pertanyaan ke Gemini.
* Mengembalikan response kepada UI.

Contoh inisialisasi:

```python
self.client = genai.Client(
    api_key=api_key
)
```

Kemudian conversation dibuat menggunakan:

```python
self.chat = self.client.chats.create(
    model=MODEL_NAME,
    config={
        "system_instruction": SYSTEM_INSTRUCTION
    }
)
```

Dengan demikian, conversation memiliki konteks dan aturan yang telah ditentukan sejak awal.

---

# 🧠 Domain Restriction

Salah satu bagian penting dari project ini adalah **System Instruction**.

AI diberikan instruksi agar hanya menjawab pertanyaan yang berhubungan dengan Programming dan IT.

Contohnya:

```text
User:
Bagaimana cara membuat REST API menggunakan Laravel?

AI:
[Menjawab pertanyaan]
```

Sedangkan:

```text
User:
Bagaimana cara memasak nasi?

AI:
Maaf, saya hanya dapat membantu pertanyaan
yang berkaitan dengan Programming, IT,
Computer Science, Software Engineering,
dan teknologi komputer.
```

Tujuannya adalah membuat chatbot memiliki **fokus domain**, bukan menjadi chatbot general-purpose.

---

# 🚫 Internet Search Restriction

Chatbot ini tidak diberikan akses terhadap tool pencarian internet.

Dengan kata lain, aplikasi tidak menggunakan:

```text
Google Search
Web Search
Web Scraping
Search Engine API
Google Search Grounding
```

Gemini hanya menerima prompt dan menghasilkan response berdasarkan model serta conversation context.

Arsitekturnya:

```text
                  User
                    │
                    ▼
             ┌─────────────┐
             │ CustomTkinter│
             │     UI      │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │ Programming │
             │     AI      │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │   Gemini    │
             │     API     │
             └─────────────┘

                    ✕
              No Web Search
```

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Masuk ke folder project:

```bash
cd REPOSITORY
```

---

## 2. Buat Virtual Environment

Disarankan menggunakan virtual environment agar dependency project tidak bercampur dengan package Python lainnya.

### Windows

```bash
python -m venv .venv
```

Aktifkan:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Aktifkan:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```text
google-genai
customtkinter
```

---

# 🔑 Gemini API Key

Aplikasi membutuhkan **Gemini API Key** untuk berkomunikasi dengan Gemini API.

Ketika aplikasi dijalankan, masukkan API Key pada:

```text
Gemini API Key: [********************] [Connect]
```

Kemudian tekan:

```text
Connect
```

Setelah berhasil terhubung, chatbot siap digunakan.

---

# ▶️ Running the Application

Jalankan:

```bash
python main.py
```

Kemudian aplikasi GUI akan terbuka.

Alur penggunaan:

```text
1. Jalankan aplikasi
        │
        ▼
2. Masukkan Gemini API Key
        │
        ▼
3. Klik Connect
        │
        ▼
4. Tulis pertanyaan
        │
        ▼
5. Klik Send
        │
        ▼
6. Gemini memberikan response
```

---

# 💬 Example Questions

Chatbot dapat digunakan untuk pertanyaan seperti:

```text
Apa perbedaan stack dan heap?
```

```text
Bagaimana cara membuat REST API menggunakan Laravel?
```

```text
Jelaskan konsep Object Oriented Programming.
```

```text
Apa fungsi Docker?
```

```text
Apa perbedaan TCP dan UDP?
```

```text
Bagaimana cara kerja garbage collector?
```

```text
Apa perbedaan process dan thread?
```

Namun pertanyaan di luar domain IT akan ditolak.

---

# 🔐 API Key Security

API Key **tidak disimpan secara hard-coded di source code**.

User memasukkan API Key melalui GUI:

```python
self.api_entry = ctk.CTkEntry(
    ...,
    show="*"
)
```

Karakter API Key akan disembunyikan pada UI.

> ⚠️ **Jangan pernah memasukkan API Key ke dalam source code atau meng-upload API Key ke GitHub.**

Contoh yang **tidak boleh dilakukan**:

```python
API_KEY = "AIzaSyXXXXXXXXXXXXXXXX"
```

Jangan commit API Key ke repository public.

---

# 📖 Code Flow

Secara keseluruhan, aplikasi bekerja seperti berikut:

```text
                   ┌───────────┐
                   │   User    │
                   └─────┬─────┘
                         │
                         ▼
                ┌─────────────────┐
                │  CustomTkinter  │
                │       UI        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  ProgrammingAI  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Gemini API    │
                └────────┬────────┘
                         │
                         ▼
                    AI Response
                         │
                         ▼
                ┌─────────────────┐
                │  Chat Interface │
                └─────────────────┘
```

---

# 🧩 Separation of Responsibilities

Project ini sengaja memisahkan UI dan AI engine.

```text
main.py
   │
   ├── ui.py
   │     └── User Interface
   │
   └── ai.py
         └── Gemini / AI Logic
```

Keuntungan pendekatan ini adalah setiap bagian mempunyai tanggung jawab yang jelas.

Misalnya jika suatu saat ingin mengganti Gemini dengan model lain, perubahan utama dapat dilakukan pada:

```text
ai.py
```

tanpa harus membangun ulang seluruh UI.

---

# 🔮 Possible Future Improvements

Project ini masih merupakan versi awal dan dapat dikembangkan lebih lanjut.

Beberapa fitur yang dapat ditambahkan:

* [ ] Markdown rendering
* [ ] Syntax highlighting untuk source code
* [ ] Streaming response
* [ ] Chat history
* [ ] Export conversation
* [ ] Clear conversation
* [ ] Dark / Light mode
* [ ] Better domain classifier
* [ ] Local model support
* [ ] Packaging menjadi `.exe`
* [ ] Persistent configuration
* [ ] Improved error handling
* [ ] Token usage monitoring

---

# ⚠️ Important Notice

Project ini menggunakan **Google Gemini API**, sehingga penggunaan API bergantung pada kebijakan, limit, dan pricing Google.

Untuk penggunaan ringan atau eksperimen, free tier dapat digunakan apabila tersedia dan sesuai dengan ketentuan akun/API saat ini.

Namun, apabila ingin mendapatkan **limit penggunaan dan performa yang lebih besar**, Anda mungkin perlu menggunakan **Google Gemini API dengan billing/paid usage yang sesuai**.

> 💳 **Perhatikan bahwa penggunaan API berbayar dapat menimbulkan biaya. Pastikan memahami pricing, quota, dan billing Google sebelum menggunakannya dalam skala besar.**

Jangan menganggap API berbayar berarti penggunaan tidak terbatas. Biaya dan limit tetap bergantung pada model, jumlah token, request, serta kebijakan pricing Google yang berlaku.

---

# 👨‍💻 Author

Created as a **Final Project** for the

**Hacktiv8 Indonesia — AI & LLM Training**

📅 **21–25 September 2026**

---

<p align="center">
  Made with ❤️ using Python & Google Gemini
</p>
