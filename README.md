# 2D Shapes Image Classifier
We aim to build a simple web platform where we showcase our small project for detection of shapes of common and uncommon objects.

> **Goal**: Build and deploy a shape detection model for common and uncommon objects.
> **Team**: Group 7 AIDI-2001-02
> **Assignment Title**: Final Project

[![Kill 'em](https://forthebadge.com/images/badges/oooo-kill-em.svg)](https://forthebadge.com) 
[![Built with](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
[![Makes People smile](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)

The field of artificial intelligence has applications in numerous parts of our lives, from manufacturing of the goods and services we consume to improving our security. With a significant growth in computer vision technology over the past five years, object detection and segmentation has become part of many applications being developed today. Object detection with the numerous large datasets, like COCO, has provided consistent and reliable computer vision models to be open-sourced. One area of computer vision that has not been widely explored is the ability to classify objects by their shape.
Shape detection for objects is an area that does not seem to have many real- world applications but is a topic that is important enough to be taught to children. Some of the niche applications of shape detection would be in manufacturing processes (for quality checks, etc.) and developing bionic arms. Understanding the shape of an object can be beneficial in those scenarios.

> **Therefore, for this project, we decided to take on the challenge of detecting 2D shapes of common and uncommon objects.**

Why 2D shapes? Firstly, defining the shape of an object is not easy as it might sound. What would be the shape of pencil, window, bowl, or plate? Just look around you and identify at five objects that you and your neighbor will agree upon. What are some 3D shapes you can think of? It is difficult to have a conventional system for 3D shapes. For 2D shapes that is easier. Therefore, we decided to begin with 2D shape detection instead of 3D. The following shapes are considered:
* Circle
* Triangle
* __*Square*__
* __*Rectangle*__
* Pentagon
* Hexagon

> __*Tricky*__: we can expect classifying a square and a rectangle to be the most challenging task.

**Input**: an image and object to be detected
**Output**: Shape prediction and confidence of prediction.
