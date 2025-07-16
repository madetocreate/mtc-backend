# Task 3

**Prompt:** Create a footer section with links, logo, copyright info, and dark styling. Make it compact and elegant.

**Result:**
Based on your request, here's some HTML code complemented with CSS:

```html
<footer>
    <div class="footer-wrapper">
        <div class="logo-section">
            <img src="your-logo-link.jpg" alt="Logo">
        </div>
        <div class="links-section">
            <a href="#">Link 1</a>
            <a href="#">Link 2</a>
            <a href="#">Link 3</a>
        </div>
        <div class="copyright-section">
            <p>&copy; 2022 Your Company Name. All rights reserved.</p>
        </div>
    </div>
</footer>
```

And some CSS to style it:

```css
footer {
    background-color: #1a1a1a;
    color: #999999;
    padding: 20px;
}

.footer-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.logo-section img {
   max-width: 100px;
}

.links-section {
    display: flex;
    gap: 20px;
}

.links-section a {
    text-decoration: none;
    color: #999999;
}

.links-section a:hover {
    color: #ffffff;
}

.copyright-section p {
    margin: 0;
    font-size: 14px;
}
```
Remember to replace "your-logo-link.jpg" with the actual path of your logo. Also, adjust the links and the company name according to your needs.
