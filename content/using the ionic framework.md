Title: Ionic vs Bootstrap
Date: 2014-4-18 15:10
Category: web development
Tags: ionic, javascript, css, web development, development
Status: draft


I come from the before times. The times where PHP was it, many were switching from *tables* to *css*, Al Gore had his
presidency stolen and you got help from some weird phpBB forum post where the signatures took up half the screen--and
you LIKED IT!

<p align="center" style="margin: 50px;">
    <img src="../images/ionic/land_before_time.jpg" alt="Land Before Time"><br>
    <i><small>I need a more ominous before picture...</small></i>
</p>

If that's how I think of the times before [Bootstrap](), how will I think of Bootstrap 5 years from now?





## Why write this?

I am writing this as a tool to help me learn more about Ionic and Bootstrap to decide which, if either, library to use
for my new hybrid web app. My app has to look good and function well on desktop, tablet and mobile.

I haven't used Ionic much, yet, but I have used Bootstrap for over a dozen projects. I love bootstrap, but there are some
things that definitely bug me and I'd love to learn about some alternatives.






## Pain points of Bootstrap

### Grid system

Columns. Rows. Grids.

It's only getting more complex with `.col-md-12`, `.col-xs-12` and such. These things aren't hard to learn, but I had just
gotten the hang of doing the whole `.container` `.row` `.span` dance. Oh, don't forget `.row-fluid` was awesome, too.

```html
<div class="container">
    <div class="row">
        <div class="span12">
        </div>
    </div>
</div>
```





## Things Bootstrap does right

### Great documentation

Boy did they nail it. I feel like Bootstrap had the best documentation of any library a couple years ago, and it still
may hold that title. It's a snap to find what you are looking for, the explanations are easy to understand and there are
examples for everything.





## Ionic's iconic integral items (pros)

### Grid system, 'yall

Shit is written with [FLEXBOX]()! I have been waiting for some kind of support for this forever, a good friend of mine
[Levi Thomason]() tried to explain it to my glazed over eyes but I think I caught the jist. Flexbox solves a ton of
problems that are normally solved with floats, tricks, and wizardry:

1. Vertical align
2. Things fill in remaining space easily
3. Elements stay where they should (footer stuck to bottom of screen)
4. etc. etc.

### AngularJS instead of jQuery

Ionic is built on top of AngularJS for all of the interactions, that is awesome. AngularJS makes writing front end
stuff so much less painful and so much easier to test. Way back when I couldn't imagine writing tests for jQuery stuff,
how would I emulate so many DOM elements?

AngularJS helps you write unit-testable code by abstracting away the DOM, instead you play around in a `$scope`
where all data is stored.





## Ionic's inconceivable integrations (cons)

### Kind of confusing docs/dist

Maybe it's because I am so used to how Bootstrap has everything laid out, but it just feels a little wonky sometimes.

I was trying to find out what exactly is in the zip distribution file and I was confused about `ionic.bundle.js` vs
`ionic.js` or `ionic-angular.js`. It's probably something that's a given to most front end developers, but I didn't
understand it.

### Purely mobile

Ionic is built only for mobile, which is a big problem for me because I want to design a hybrid mobile/desktop app.





## Conclusion

Ionic seems to only support mobile

I am going to give Ionic a shot for my next website even though it only seems to support mobile






## All jokes aside

I am a developer, mostly backend. I am not a great designer. I don't have "that eye." Any design that by some
happenstance ends up being good is usually due to iteration after iteration with generous advice and critique.

I am a shoot from the hip kind of guy, I like to do things fast&mdash;if I messed up on any details about Bootstrap or
Ionic, please correct me!

Is something easier than I am making it seem? Am I doing something wrong? Let me know!
