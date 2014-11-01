Title: Summary tool under JavaScript
Date: 2014-10-31 16:02
Category: JS
Tags: JS, JavaScript, Content-summary
Author: Andrew V.
Summary: Implementation of summarizing content in javascript

This algorithm was found in [the Internet](http://thetokenizer.com/2013/04/28/build-your-own-summary-tool/)
As at this moment I try to implement add-on for Firefox, and some function I've needed was to summarize web-content.

So the main Idea of the algorithm is to build matrix of mutual sentences intersection which is calculates by counting the same words in two sections and division this count with avarage sentence length in words.

Than we summarize intersactions for every sentence and with this value choise what sentence should be used in summary.

This algorithm I've implemented in javascript, so the source is [here](http://kostyll.github.io/summary.js/)

