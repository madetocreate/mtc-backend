# Task 1

**Prompt:** Create a dark-themed hero section for the AION landing page using Tailwind CSS. Include a headline, subheadline, CTA button, and futuristic styling with animations.

**Result:**
Sure, I'll provide the basic HTML structure and styles of the hero section with Tailwind CSS. 

Since Tailwind doesn't support animations out of the box, we'll use some basic keyframes and add AOS (Animate On Scroll) library to handle the animation.

The HTML code:

```html
<div class="hero w-screen h-screen bg-black flex items-center justify-center text-white">
  <div class="container mx-auto px-4" data-aos="fade-up">
      <h1 class="text-5xl font-bold mb-4">Welcome to AION</h1>
      <p class="text-2xl mb-8">Experience The Future of AI Today</p>
      <button class="btn text-2xl font-bold py-2 px-4 rounded-full bg-blue-500 hover:bg-blue-400 text-white">Get Started</button>
  </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
```

Tailwind CSS is a utility-first CSS framework that doesn't have built-in animations. You would need to use an extra library like AOS or write custom CSS to do animations. Above, we are using AOS and CDN provided to load it.

To init the AOS library add following script tag after all HTML:

```html
<script>
  AOS.init({
    duration: 1200,
  })
</script>
```

Ensure to add the Tailwind CSS and AOS CSS paths in your HTML file's head section:

```html
<head>
  <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
</head>
```

This will give you a full-screen hero section with an animated introductory text and a call-to-action button. The section will fade in when the page is loaded. Please note, you'll need to adjust the styling as per your design specifications. Also, ensure to install all necessary libraries and include the right paths for your project.
  
Keep in mind that Tailwind CSS purges unused classes in production, so ensure to keep the classes you are using in production explicitly in your code.
