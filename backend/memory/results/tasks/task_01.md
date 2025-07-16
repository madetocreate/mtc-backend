# Task 1

**Prompt:** Create a dark-themed hero section for the AION landing page using Tailwind CSS. Include a headline, subheadline, CTA button, and futuristic styling with animations.

**Result:**
Sure, here's an example of a dark-themed hero section for an AION landing page.

HTML:

```html
<div class="bg-gray-900 text-white py-20 px-6">
  <div class="container mx-auto text-center">
    <h1 class="text-5xl font-bold mb-4 animate-pulse">Welcome to AION</h1>
    <h2 class="text-3xl mb-8 animate-bounce">Revolutionizing the Future</h2>
    <button class="px-6 py-3 bg-indigo-700 text-white text-sm font-semibold rounded-lg">Explore now</button>
  </div>
</div>
```

CSS:

In this case, I'm not adding any CSS as we are using Tailwind CSS, a utility-first CSS framework where we have defined most of our styles and animations directly in our HTML. The `bg-gray-900` is making the background dark. The `text-white` is making the text color white. 

In this hero section, we've added some animations to the titles. The main headline has a pulse animation and the subheadline has a bounce animation. 

The button has a `bg-indigo-700` which gives it a darker tone that goes along with the dark theme. The rounded corners are added using `rounded-lg`.

Please get Tailwind CSS installed and setup correctly if you haven't done so before attempting to use this code or animations and utility classes will not work.

And note that the actual animation and exact look will depend on the Tailwind CSS version and configurations that you have. Furthermore, I have kept the page simple for now, but you could use other Tailwind CSS classes to further configure and style your dark-themed hero section.
