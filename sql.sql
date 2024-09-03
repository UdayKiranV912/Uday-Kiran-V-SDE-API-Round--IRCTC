/* General Styles */
body {
  font-family: Arial, sans-serif;
}

/* Pop-up Form Styles */
.popup-form {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.form-content {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

/* Slider Styles */
.slider {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
}
.slides {
  display: flex;
  transition: transform 0.5s ease-in-out;
}
.slide {
  width: 100%;
  height: 100%;
}
.dots {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
.dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ccc;
  margin: 0 5px;
  cursor: pointer;
}
.dot.active {
  background-color: #333;
}

/* Our Project Styles */
.project-img {
  display: none;
  width: 100%;
  height: auto;
}
.project-img.active {
  display: block;
}

/* Highlight on Hover Styles */
.card {
  width: 200px;
  height: 100px;
  background-color: #f4f4f4;
  margin: 10px;
  display: inline-block;
  transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}
