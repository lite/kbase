//
//  PopoverDemoViewController.m
//  PopoverDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "PopoverDemoViewController.h"
#import "FontChooserViewController.h"

@implementation PopoverDemoViewController

@synthesize allText, popOver;

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

- (void) fontSelected:(NSString *)fontName;
{
    allText.font = [UIFont fontWithName:fontName size:18.0f];
}

- (IBAction) buttonTapped:(id) sender
{
//    NSLog(@"buttonTapped.");
    
    if( [popOver isPopoverVisible]){
        [popOver dismissPopoverAnimated:YES];
    }else{
        FontChooserViewController *fc = [[FontChooserViewController alloc ] init];
        fc.delegate = self;
        popOver = [[UIPopoverController alloc] initWithContentViewController:fc];
        [fc autorelease];

        popOver.popoverContentSize = CGSizeMake(250, 260);
        [popOver presentPopoverFromBarButtonItem:sender 
                                        permittedArrowDirections:UIPopoverArrowDirectionAny
                                        animated:YES];
    
    }
}

@end
