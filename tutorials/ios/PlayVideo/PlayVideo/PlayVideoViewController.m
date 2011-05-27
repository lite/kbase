//
//  PlayVideoViewController.m
//  PlayVideo
//
//  Created by dennisli on 3/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "PlayVideoViewController.h"

@implementation PlayVideoViewController

- (IBAction) buttonTapped:(id)sender
{
    NSString* path = [ [NSBundle mainBundle ] pathForResource:@"0901 Goodbye" ofType:@"mov"];

    player = [[MPMoviePlayerViewController alloc] initWithContentURL:[NSURL fileURLWithPath:path]];
    
//    player.moviePlayer.scalingMode = MPMovieScalingModeFill;
//    player.moviePlayer.shouldAutoplay = NO;
    [ [NSNotificationCenter defaultCenter] addObserver:self 
                                              selector:@selector(movieFinishedPlaying:) 
                                                  name:MPMoviePlayerPlaybackDidFinishNotification
                                                object:[player moviePlayer]];
    
    [self presentMoviePlayerViewControllerAnimated:player];
}

- (void) movieFinishedPlaying:(NSNotification* )note
{
    [[NSNotificationCenter defaultCenter] removeObserver:self 
                                                    name:MPMoviePlayerPlaybackDidFinishNotification 
                                                  object:[player moviePlayer]];
    NSLog(@"movieFinishedPlaying.");
    [player release];
}

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

/*
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad
{
    [super viewDidLoad];
}
*/

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
