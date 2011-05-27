//
//  FontChooserViewController.m
//  PopoverDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "FontChooserViewController.h"


@implementation FontChooserViewController

@synthesize delegate;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
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

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
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

- (IBAction) buttonTapped:(id) sender
{
    UIButton* temp = (UIButton*) sender;
    NSString* font = [temp titleForState:UIControlStateNormal];
    if(delegate){
        [delegate fontSelected:font];
    }
}

@end
