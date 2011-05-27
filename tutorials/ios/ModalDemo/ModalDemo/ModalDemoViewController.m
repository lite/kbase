//
//  ModalDemoViewController.m
//  ModalDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "ModalDemoViewController.h"

@implementation ModalDemoViewController

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

- (IBAction) buttonTapped:(id)sender
{
//    NSLog(@"buttonTapped.");
    InstrusiveViewController* ivc = [[InstrusiveViewController alloc] init];
    ivc.delegate = self;
    
    UINavigationController* nc = [[UINavigationController alloc] initWithRootViewController:ivc];

//    nc.modalPresentationStyle = UIModalPresentationFullScreen;
//    nc.modalPresentationStyle = UIModalPresentationPageSheet;
    nc.modalPresentationStyle = UIModalPresentationFormSheet;
    [self presentModalViewController:nc animated:YES];
    
    [ivc release];
    [nc release];
}


- (void) doneButtonPressed:(NSArray *)values
{
//    NSLog(@"doneButtonPressed.");
    [self dismissModalViewControllerAnimated:YES];
    
    NSString* message = [NSString stringWithFormat:@"The values were %@, %@ and %@", 
                     [values objectAtIndex:0], [values objectAtIndex:1], [values objectAtIndex:2]];
    
    UIAlertView* alert = [[UIAlertView alloc] 
                          initWithTitle:@"Value passed" 
                          message:message delegate:nil 
                          cancelButtonTitle:@"Excellent" 
                          otherButtonTitles:nil];
    
    [alert show];
    [alert release];
}

@end
