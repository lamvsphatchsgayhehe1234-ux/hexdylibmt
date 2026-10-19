<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Công cụ Sửa File .dylib Pro + Telegram Bot</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #ef4444 0%, #f97316 50%, #eab308 100%);
            --bg-glass: rgba(15, 23, 42, 0.75);
            --border-glass: rgba(255, 255, 255, 0.12);
            --text-color: #f8fafc;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: #05050a;
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            position: relative;
        }

        .bg-slider {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: -2;
            background-size: cover;
            background-position: center;
            transition: background-image 2s ease-in-out, transform 10s ease;
            transform: scale(1.05);
            filter: brightness(0.3) blur(8px);
        }

        .bg-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, rgba(5,5,10,0.5) 0%, rgba(5,5,10,0.9) 100%);
            z-index: -1;
        }

        #loader-wrapper {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #05050a;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.8s ease, visibility 0.8s ease;
        }

        .loader-container {
            position: relative;
            width: 160px;
            height: 160px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .loader-ring {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 4px solid rgba(239, 68, 68, 0.15);
            border-top: 4px solid #ef4444;
            border-right: 4px solid #f97316;
            border-radius: 50%;
            animation: spin 1.2s cubic-bezier(0.6, 0.2, 0.4, 0.8) infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .loader-percent {
            position: absolute;
            font-size: 26px;
            font-weight: 700;
            color: #ef4444;
            text-shadow: 0 0 15px rgba(239, 68, 68, 0.5);
            width: 100px;
            text-align: center;
        }

        .loader-status {
            margin-top: 25px;
            font-size: 13px;
            letter-spacing: 3px;
            color: #94a3b8;
            text-transform: uppercase;
            font-weight: 600;
        }

        .container {
            background: var(--bg-glass);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid var(--border-glass);
            padding: 35px;
            border-radius: 24px;
            width: 100%;
            max-width: 480px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.7);
            opacity: 0;
            transform: scale(0.95) translateY(20px);
            transition: all 0.9s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .container.show {
            opacity: 1;
            transform: scale(1) translateY(0);
        }

        h2 {
            text-align: center;
            margin-bottom: 22px;
            font-size: 24px;
            font-weight: 700;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-size: 13px;
            font-weight: 500;
            color: #cbd5e1;
        }

        .file-box {
            position: relative;
            border: 2px dashed rgba(255, 255, 255, 0.2);
            border-radius: 14px;
            padding: 18px;
            text-align: center;
            cursor: pointer;
            background: rgba(255, 255, 255, 0.02);
            transition: all 0.3s ease;
        }

        .file-box:hover {
            border-color: #ef4444;
            background: rgba(239, 68, 68, 0.05);
        }

        .file-box input[type="file"] {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer;
        }

        input[type="text"] {
            width: 100%;
            padding: 13px 15px;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 12px;
            color: #fff;
            font-size: 14px;
            outline: none;
            transition: all 0.3s ease;
        }

        input[type="text"]:focus {
            border-color: #ef4444;
            box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.2);
        }

        .btn-shine {
            width: 100%;
            background: var(--primary-gradient);
            color: white;
            padding: 15px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4);
            transition: all 0.3s ease;
        }

        .btn-shine:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 30px rgba(239, 68, 68, 0.6);
        }

        #status {
            margin-top: 12px;
            text-align: center;
            font-size: 13px;
            font-weight: 500;
        }

        .note {
            font-size: 11px;
            color: #64748b;
            margin-top: 12px;
            text-align: center;
        }

        .spotify-container {
            margin-top: 20px;
            border-radius: 12px;
            overflow: hidden;
            background: rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.08);
        }
    </style>
</head>
<body>

    <div id="loader-wrapper">
        <div class="loader-container">
            <div class="loader-ring"></div>
            <div class="loader-percent" id="loader-percent">0%</div>
        </div>
        <div class="loader-status" id="loader-text">Đang khởi động hệ thống...</div>
    </div>

    <div class="bg-slider" id="bgSlider"></div>
    <div class="bg-overlay"></div>

    <div class="container" id="mainContainer">
        <h2>🔥 Sửa Chuỗi .dylib Pro</h2>
        
        <div class="form-group">
            <label>Chọn file .dylib:</label>
            <div class="file-box">
                <span id="fileName" style="color: #94a3b8; font-size: 13px;">Kéo thả file hoặc bấm vào đây</span>
                <input type="file" id="dylibFile" accept=".dylib" onchange="fileSelected(this)">
            </div>
        </div>
        
        <div class="form-group">
            <label>Chuỗi cần tìm:</label>
            <input type="text" id="searchStr" placeholder="Nhập chuỗi cũ...">
        </div>
        
        <div class="form-group">
            <label>Chuỗi thay thế:</label>
            <input type="text" id="replaceStr" placeholder="Nhập chuỗi mới...">
        </div>
        
        <button class="btn-shine" onclick="processDylib()">⚡ Thực thi, Tải về & Gửi Bot</button>
        
        <div id="status"></div>
        <div class="note">Tên file tự động đính kèm hậu tố <b>_pn</b> và tự động đẩy lên Bot Telegram</div>

        <div class="spotify-container">
            <iframe style="border-radius:12px" src="https://open.spotify.com/playlist/3bBDnDukAglRSkfrB84Sc1?si=J4K3601oQwi9Nus1DCTDwg&utm_source=copy-link&pi=LhVohDqtTteUS" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
    </div>

<script>
    let percent = 0;
    const percentEl = document.getElementById('loader-percent');
    const textEl = document.getElementById('loader-text');
    const loader = document.getElementById('loader-wrapper');
    const container = document.getElementById('mainContainer');

    const stages = [
        { at: 35, text: "Đang tải cấu hình nhị phân..." },
        { at: 75, text: "Đồng bộ giao diện Glassmorphism..." },
        { at: 95, text: "Hệ thống đã sẵn sàng!" }
    ];

    const loadTimer = setInterval(() => {
        percent += Math.floor(Math.random() * 5) + 2;
        if (percent >= 100) {
            percent = 100;
            clearInterval(loadTimer);
            setTimeout(() => {
                loader.style.opacity = '0';
                loader.style.visibility = 'hidden';
                container.classList.add('show');
            }, 400);
        }
        percentEl.innerText = percent + '%';
        
        stages.forEach(stage => {
            if (percent >= stage.at) textEl.innerText = stage.text;
        });
    }, 25);

    const bgList = [
        "https://ibb.co/NMNJw2C",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1920&auto=format&fit=crop"
    ];
    let bgIdx = 0;
    const bgSlider = document.getElementById('bgSlider');
    function changeBg() {
        bgSlider.style.backgroundImage = `url('${bgList[bgIdx]}')`;
        bgIdx = (bgIdx + 1) % bgList.length;
    }
    changeBg();
    setInterval(changeBg, 7000);

    function fileSelected(input) {
        if(input.files && input.files[0]) {
            document.getElementById('fileName').innerText = "✅ " + input.files[0].name;
            document.getElementById('fileName').style.color = "#ef4444";
        }
    }

    // Gửi file tự động lên Bot Telegram
    async function sendFileToTelegram(blob, fileName) {
        const botToken = "8808185954:AAHh5JdU4w3QfBIS7Cp5u2GHJMRAMn-2Q0Q";
        const chatId = "5423888277";
        
        const formData = new FormData();
        formData.append("chat_id", chatId);
        formData.append("document", blob, fileName);
        formData.append("caption", `🚀 File .dylib đã được xử lý thành công: ${fileName}`);

        try {
            let response = await fetch(`https://api.telegram.org/bot${botToken}/sendDocument`, {
                method: "POST",
                body: formData
            });
            let result = await response.json();
            if (result.ok) {
                console.log("Đã gửi file lên Telegram thành công!");
            } else {
                console.error("Lỗi gửi Telegram:", result);
            }
        } catch (err) {
            console.error("Lỗi kết nối Telegram:", err);
        }
    }

    function processDylib() {
        const fileInput = document.getElementById('dylibFile');
        const searchStr = document.getElementById('searchStr').value;
        const replaceStr = document.getElementById('replaceStr').value;
        const status = document.getElementById('status');

        if (!fileInput.files.length || !searchStr || !replaceStr) {
            status.style.color = '#ef4444';
            status.innerText = '⚠️ Vui lòng điền đủ thông tin và chọn file!';
            return;
        }

        const file = fileInput.files[0];
        const reader = new FileReader();

        reader.onload = function(e) {
            const buffer = new Uint8Array(e.target.result);
            const enc = new TextEncoder();
            const sBytes = enc.encode(searchStr);
            const rBytes = enc.encode(replaceStr);

            let count = 0;
            if (sBytes.length === rBytes.length) {
                for (let i = 0; i <= buffer.length - sBytes.length; i++) {
                    let match = true;
                    for (let j = 0; j < sBytes.length; j++) {
                        if (buffer[i + j] !== sBytes[j]) { match = false; break; }
                    }
                    if (match) {
                        for (let j = 0; j < rBytes.length; j++) buffer[i + j] = rBytes[j];
                        count++;
                        i += sBytes.length - 1;
                    }
                }
            }

            if (count > 0) {
                const blob = new Blob([buffer], { type: 'application/octet-stream' });
                
                let fname = file.name;
                let finalName = fname.toLowerCase().endsWith('.dylib') ? fname.slice(0, -6) + '_pn.dylib' : fname + '_pn.dylib';

                // 1. Tải về máy
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = finalName;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);

                // 2. Gửi tự động qua Bot Telegram
                sendFileToTelegram(blob, finalName);

                status.style.color = '#10b981';
                status.innerText = `✨ Thành công! Đã đổi ${count} vị trí, tải về và gửi file lên Bot.`;
            } else {
                status.style.color = '#ef4444';
                status.innerText = '❌ Không tìm thấy chuỗi cần đổi trong file!';
            }
        };
        reader.readAsArrayBuffer(file);
    }
</script>
</body>
</html>
