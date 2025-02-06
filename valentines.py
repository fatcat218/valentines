<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valentine's Day</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Roboto:wght@400&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Dancing Script', cursive;
            background: linear-gradient(135deg, #ffe4e1, #ffb6c1);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            position: relative;
        }
        .container {
            text-align: center;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            animation: fadeIn 1s ease-in-out;
        }
        .container img {
            max-width: 80%;
            height: auto;
            border-radius: 10px;
        }
        .text {
            font-size: 2.5rem;
            margin: 20px 0;
            color: #5a189a;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        .button {
            padding: 15px 25px;
            font-size: 1.2rem;
            font-family: 'Roboto', sans-serif;
            color: #ffffff;
            background: linear-gradient(45deg, #ff6ec4, #7873f5);
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .button:hover {
            background: linear-gradient(45deg, #7873f5, #ff6ec4);
            transform: scale(1.1);
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        .hidden {
            display: none;
        }
        .decorations {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }
        .decorations .flower {
            position: absolute;
            width: 100px;
            height: 100px;
            background: url('flower.png') no-repeat center;
            background-size: contain;
            animation: float 6s infinite ease-in-out;
        }
        .decorations .flower:nth-child(1) {
            top: 10%;
            left: 20%;
            animation-delay: 0s;
        }
        .decorations .flower:nth-child(2) {
            top: 50%;
            left: 70%;
            animation-delay: 2s;
        }
        .decorations .flower:nth-child(3) {
            top: 80%;
            left: 30%;
            animation-delay: 4s;
        }
        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-20px);
            }
        }
    </style>
</head>
<body>
    <div class="decorations">
        <div class="flower"></div>
        <div class="flower"></div>
        <div class="flower"></div>
    </div>
    <div id="slide1" class="container">
        <img src="dog1.jpg" alt="First Image">
        <div class="text">Will you be my Valentine?</div>
        <button class="button" onclick="nextSlide(2)">Yes!</button>
    </div>

    <div id="slide2" class="container hidden">
        <img src="dog2.jpg" alt="Second Image">
        <div class="text">What time are you free on 14th February?</div>
        <button class="button" onclick="nextSlide(3)">After 5 PM</button>
        <button class="button" onclick="nextSlide(3)">After 7 PM</button>
        <button class="button" onclick="nextSlide(3)">After 9 PM</button>
    </div>

    <div id="slide3" class="container hidden">
        <div class="text">What do you want to do together?</div>
        <button class="button" onclick="nextSlide(4)">Watch a movie and eat good food</button>
        <button class="button" onclick="nextSlide(4)">I take you out to watch the sunset</button>
        <button class="button" onclick="nextSlide(4)">Or maybe whatever idea you have :)</button>
    </div>

    <div id="slide4" class="container hidden">
        <img src="puppies.jpg" alt="Final Image">
        <div class="text">
            Thank you for being my Valentine, my first and only Valentine ever. You make every moment of my life magical. 
            I will always love you, cherish you, and let’s just say, I’ll be wifing you up in every way possible. 
            You’re my dream, my everything, and the best thing to ever happen to me. Here’s to a lifetime of love, passion, and moments that make the stars jealous.
        </div>
        <button class="button" onclick="nextSlide(1)">Restart</button>
    </div>

    <script>
        function nextSlide(slideNumber) {
            // Hide all slides
            document.querySelectorAll('.container').forEach(slide => {
                slide.classList.add('hidden');
            });
            // Show the selected slide
            document.getElementById('slide' + slideNumber).classList.remove('hidden');
        }
    </script>
</body>
</html>
