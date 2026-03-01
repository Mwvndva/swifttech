import codecs
import re

filepath = r'c:\Users\Administrator\Downloads\swifttech\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    text = f.read()

# Replace CSS
css_old = """        .phone-card {
            flex-shrink: 0;
            width: 220px;
            background: var(--card);
            border-radius: 24px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }

        .phone-card:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: rgba(0, 212, 255, 0.4);
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.15);
        }

        .phone-img {
            width: 100%;
            height: 260px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }

        .phone-silhouette {
            font-size: 100px;
            line-height: 1;
            filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.3));
        }

        .phone-img-bg {
            position: absolute;
            inset: 0;
            opacity: 0.15;
        }

        .phone-info {
            padding: 16px 20px 20px;
            text-align: left;
        }"""

css_new = """        .phone-card {
            flex-shrink: 0;
            width: 280px;
            background: rgba(17, 17, 17, 0.8);
            backdrop-filter: blur(12px);
            border-radius: 24px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08); /* slightly higher visibility */
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color 0.3s, box-shadow 0.3s;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }

        .phone-card:hover {
            transform: translateY(-12px) scale(1.02);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.2);
        }

        .phone-img {
            width: 100%;
            height: 300px;
            position: relative;
            overflow: hidden;
        }

        .phone-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        .phone-img::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(17, 17, 17, 1) 0%, transparent 60%);
            pointer-events: none;
            z-index: 1;
        }

        .phone-card:hover .phone-img img {
            transform: scale(1.08);
        }

        .phone-info {
            padding: 24px;
            text-align: left;
            position: relative;
            z-index: 2;
            margin-top: -60px; /* Bring info over the image gradient */
        }"""

if css_old in text:
    text = text.replace(css_old, css_new)
    print("CSS replaced")
else:
    print("CSS NOT replaced")

html_pattern = r'<div class="carousel-wrapper">.*?</div>\s*</div>\s*</section>'
html_new = '''<div class="carousel-wrapper">
            <div class="carousel-track" id="carousel">

                <!-- Cards duplicated for infinite loop -->
                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1605236453806-6ff36851218e?auto=format&fit=crop&q=80&w=600" alt="iPhone 15 Pro">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 15 Pro</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?auto=format&fit=crop&q=80&w=600" alt="Galaxy S25">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Samsung</div>
                        <div class="phone-name">Galaxy S25</div>
                        <span class="phone-tag tag-hot">Hot 🔥</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1591337676887-a4bba6607341?auto=format&fit=crop&q=80&w=600" alt="iPhone 14">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 14</div>
                        <span class="phone-tag tag-ex">Ex UK</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&q=80&w=600" alt="14 Ultra">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Xiaomi</div>
                        <div class="phone-name">14 Ultra</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1601784551446-20c9e07cd56e?auto=format&fit=crop&q=80&w=600" alt="Galaxy A55">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Samsung</div>
                        <div class="phone-name">Galaxy A55</div>
                        <span class="phone-tag tag-ex">Ex US</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&q=80&w=600" alt="iPhone 13">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 13</div>
                        <span class="phone-tag tag-ex">Ex UK</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1546054454-aa26e2b734c7?auto=format&fit=crop&q=80&w=600" alt="Redmi Note 13">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Xiaomi</div>
                        <div class="phone-name">Redmi Note 13</div>
                        <span class="phone-tag tag-hot">Hot 🔥</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&q=80&w=600" alt="JBL Tune 510BT">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">JBL</div>
                        <div class="phone-name">Tune 510BT</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

                <!-- Duplicate for loop -->
                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1605236453806-6ff36851218e?auto=format&fit=crop&q=80&w=600" alt="iPhone 15 Pro">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 15 Pro</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?auto=format&fit=crop&q=80&w=600" alt="Galaxy S25">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Samsung</div>
                        <div class="phone-name">Galaxy S25</div>
                        <span class="phone-tag tag-hot">Hot 🔥</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1591337676887-a4bba6607341?auto=format&fit=crop&q=80&w=600" alt="iPhone 14">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 14</div>
                        <span class="phone-tag tag-ex">Ex UK</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&q=80&w=600" alt="14 Ultra">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Xiaomi</div>
                        <div class="phone-name">14 Ultra</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1601784551446-20c9e07cd56e?auto=format&fit=crop&q=80&w=600" alt="Galaxy A55">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Samsung</div>
                        <div class="phone-name">Galaxy A55</div>
                        <span class="phone-tag tag-ex">Ex US</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&q=80&w=600" alt="iPhone 13">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Apple</div>
                        <div class="phone-name">iPhone 13</div>
                        <span class="phone-tag tag-ex">Ex UK</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1546054454-aa26e2b734c7?auto=format&fit=crop&q=80&w=600" alt="Redmi Note 13">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">Xiaomi</div>
                        <div class="phone-name">Redmi Note 13</div>
                        <span class="phone-tag tag-hot">Hot 🔥</span>
                    </div>
                </div>

                <div class="phone-card">
                    <div class="phone-img">
                        <img src="https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&q=80&w=600" alt="JBL Tune 510BT">
                    </div>
                    <div class="phone-info">
                        <div class="phone-brand">JBL</div>
                        <div class="phone-name">Tune 510BT</div>
                        <span class="phone-tag tag-new">New</span>
                    </div>
                </div>

            </div>
        </div>
    </section>'''

text, count = re.subn(html_pattern, html_new, text, flags=re.DOTALL)
if count > 0:
    print('HTML replaced')
else:
    print('HTML NOT replaced')

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(text)
