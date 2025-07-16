# Task 3

**Prompt:** Create a footer section with links, logo, copyright info, and dark styling. Make it compact and elegant.

**Result:**
Sure, here is a simple and compact footer section using HTML and CSS. 

HTML:

```html
<footer class="footer-dark">
    <div class="container">
        <div class="row">
            <div class="col">
                <img src="logo.png" alt="logo">
            </div>
            <div class="col">
                <ul>
                    <li><a href="#">Link 1</a></li>
                    <li><a href="#">Link 2</a></li>
                    <li><a href="#">Link 3</a></li>
                </ul>
            </div>
            <div class="col">
                <p>&copy; YourCompany 2023.</p>
            </div>
        </div>
    </div>
</footer>
```
CSS:

```css
.footer-dark {
    padding:20px 0;
    color:#f0f9ff;
    background-color:#282d32;
    position:relative;
    bottom:0;
    width:100%;
}

.footer-dark ul {
    padding:0;
    list-style:none;
    line-height:1.6;
    color:#999999;
}

.footer-dark ul a {
    color:inherit;
    text-decoration:none;
}

.footer-dark img {
    max-width:100px;
}
```

You can replace the '#' in the `a` tags with the links you want. The `src` attribute of the `img` tag should be replaced with the path of your logo. The copyright text is currently for the year 2023 and 'YourCompany' - adapt those to fit your needs. The CSS classes .col, .row and .container are typical classes in frameworks like Bootstrap but of course you can implement them yourselves too.
