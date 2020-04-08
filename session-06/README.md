# Introduction to Variable Fonts

## What’s a variable font?
A variable font is a single font file contains many different variations of a typeface, instead of having a separate font file for every style of the type family. This format was developed in collaboration by Adobe, Apple, Google, and Microsoft.

### Advantages of variable fonts
- Font loading
	- HTTP requests
	- KB of data (depends on character set and design space)
- Purer expression of type design process
- Options!

*See more on [We Are Family! I’ve Got All My Variations With Me](https://vimeo.com/251494096) with David Jonathan Ross*

### Disadvantages of variable fonts
- Lack of support, especially in Desktop programs
- Compromised drawing flexibility — difficulty in developing compatibile outlines

## Variable Fonts and CSS
You can import a variable font in the same way as any other typeface, using the `@font-face` rule.
Variable fonts can be set by CSS, using `font-variation-settings.`

```css
@font-face {
  font-family: 'Magmatic';
  src: url('MagmaticVF.ttf') format('truetype-variations');
}

p{
  font-family: 'Magmatic', sans-serif;
  font-variation-settings: 'wght' 200,'wdth' 600; 👈
}
```

The `font-variation-settings` is the CSS property for variable fonts. 
- Values for multiple axes are separated by `,`
- Each axis name is in in between `' '` marks, with the value after it
- Standard axes for variation are in **lowercase**, custom axes are in **uppercase**

### Standard (registered) axes
|syntax| description | Non-VF equivalent 
|---|---| ---
|wght| weight | `font-weight` 
|wdth| width | `font-stretch`
|opsz| optical sizing | `font-optical-sizing`
|ital| italicization | `font-style: italic` 
|slnt| slant | `font-style: oblique` 

- Read more with the [Open Type specs](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg)
- Read a [caveat for italics](https://rwt.io/typography-tips/getting-bent-current-state-italics-variable-font-support)
