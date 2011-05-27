//
//  TapGestureViewController.m
//  TapGesture
//
//  Created by dennisli on 3/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "TapGestureViewController.h"

@implementation TapGestureViewController

@synthesize blueBox;

- (void)dealloc
{
    [super dealloc];
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad
{
    [super viewDidLoad];
    
    UITapGestureRecognizer* tapper = [[UITapGestureRecognizer alloc] 
                                      initWithTarget:self 
                                      action:@selector(tapped:)];
    UILongPressGestureRecognizer* longpress = [[UILongPressGestureRecognizer alloc] 
                                      initWithTarget:self 
                                      action:@selector(longpressed:)];
    UIPinchGestureRecognizer* pinch = [[UIPinchGestureRecognizer alloc] 
                                               initWithTarget:self 
                                               action:@selector(pinching:)];
    UISwipeGestureRecognizer* swipe = [[UISwipeGestureRecognizer alloc] 
                                       initWithTarget:self 
                                       action:@selector(swiped:)];
    UIRotationGestureRecognizer* rotation = [[UIRotationGestureRecognizer alloc] 
                                       initWithTarget:self 
                                       action:@selector(rotating:)];
    
    swipe.direction = UISwipeGestureRecognizerDirectionLeft|UISwipeGestureRecognizerDirectionRight;
    [self.view addGestureRecognizer:swipe];
    longpress.minimumPressDuration = 1;
    [blueBox addGestureRecognizer:longpress];
    [blueBox addGestureRecognizer:pinch];
    [blueBox addGestureRecognizer:tapper];
    [blueBox addGestureRecognizer:rotation];
    
    [tapper release];
    [longpress release];
    [pinch release];
    [swipe release];
    [rotation release];
}

- (void) tapped:(UITapGestureRecognizer* )sender
{
    [UIView beginAnimations:nil context:nil];
    CGFloat r = (CGFloat)random()/(CGFloat) RAND_MAX;
    CGFloat g = (CGFloat)random()/(CGFloat) RAND_MAX;
    CGFloat b = (CGFloat)random()/(CGFloat) RAND_MAX;
    blueBox.backgroundColor = [UIColor colorWithRed:r green:g blue:b alpha:1];

    [UIView commitAnimations];
}

- (void) longpressed:(UILongPressGestureRecognizer* )sender
{
    [UIView beginAnimations:nil context:nil];
    blueBox.backgroundColor = [UIColor redColor];
    [UIView commitAnimations];
}


- (void) pinching:(UIPinchGestureRecognizer* )sender
{
    CGAffineTransform myTransform =CGAffineTransformMakeScale(sender.scale, sender.scale);
    sender.view.transform = myTransform;
}

- (void) rotating:(UIRotationGestureRecognizer* )sender
{
    CGAffineTransform myTransform =CGAffineTransformMakeRotation(sender.rotation);
    sender.view.transform = myTransform;
}

- (void) swiped:(UISwipeGestureRecognizer* )sender
{
    [UIView beginAnimations:nil context:nil];
    [UIView setAnimationRepeatAutoreverses:YES];
    [UIView setAnimationRepeatCount:5];
    [UIView setAnimationDelegate:self];
    [UIView setAnimationDidStopSelector:@selector(animationStopped:)];
    blueBox.backgroundColor = [UIColor whiteColor];
    [UIView commitAnimations];
}

- (void) animationStopped:(id)sender
{
    blueBox.backgroundColor = [UIColor blueColor];
}


- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return YES;
}

@end
