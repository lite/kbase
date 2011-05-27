//
//  InstatwitViewController.m
//  Instatwit
//
//  Created by dennisli on 1/18/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "InstatwitViewController.h"

@implementation InstatwitViewController

@synthesize tweetPicker;
/*
// The designated initializer. Override to perform setup that is required before the view is loaded.
- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}
*/

/*
// Implement loadView to create a view hierarchy programmatically, without using a nib.
- (void)loadView {
}
*/


// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
    [super viewDidLoad];
	activities = [[NSArray alloc] initWithObjects:
				  @"sleeping",
				  @"eating", 
				  @"working", 
				  @"thinking", 
				  @"leaving", 
				  @"shopping", 
				  @"hello worlding", nil];
	feelings = [[NSArray alloc] initWithObjects:
				@"awesome",
				@"happy", 
				@"hopeful", nil];
}


// Override to allow orientations other than the default portrait orientation.
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    return YES;
}

- (void)didReceiveMemoryWarning {
	// Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
	
	// Release any cached data, images, etc that aren't in use.
}

- (void)viewDidUnload {
	// Release any retained subviews of the main view.
	// e.g. self.myOutlet = nil;
	[tweetPicker release];
	[activities release];
	[feelings release];
}


- (void)dealloc {
    [super dealloc];
}


- (IBAction)sendButtonTapped:(id)sender
{
	NSString* themessage = [NSString stringWithFormat:
						   @"I'm %@ and feeling %@ about it.",
						   [activities objectAtIndex:[tweetPicker selectedRowInComponent:0]],
						   [feelings objectAtIndex:[tweetPicker selectedRowInComponent:1]]];
	NSLog(themessage);
//	NSLog(@"Tweet button tapped!");	
	
	//TWITTER BLACK MAGIC
//	NSMutableURLRequest *theRequest=[NSMutableURLRequest requestWithURL:[NSURL
//																		 URLWithString:@”http://YOUR_TWITTER_USERNAME:YOUR_TWITTER_PASSWORD@twitter.com/
//																		 statuses/update.xml”]
//															cachePolicy:NSURLRequestUseProtocolCachePolicy
//														timeoutInterval:60.0];
//	[theRequest setHTTPMethod:@”POST”];
//	[theRequest setHTTPBody:[[NSString stringWithFormat:@”status=%@”,
//							  themessage] dataUsingEncoding:NSASCIIStringEncoding]];
//	NSURLResponse* response;
//	NSError* error;
//	NSData* result = [NSURLConnection sendSynchronousRequest:theRequest
//										   returningResponse:&response error:&error];
//	NSLog(@”%@”, [[[NSString alloc] initWithData:result
//										encoding:NSASCIIStringEncoding] autorelease]);
	// END TWITTER BLACK MAGIC
	
}

// datasource
- (NSInteger)numberOfComponentsInPickerView:pickerView
{
	return 2;
}

- (NSInteger)pickerView:pickerView numberOfRowsInComponent:(NSInteger)component
{
	if(component == 0){
		return [activities count];
	}else{
		return [feelings count];
	}
}

// delegate
- (NSString *)pickerView:pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
	switch(component){
		case 0:
			return [activities objectAtIndex:row];
		default:
			return [feelings objectAtIndex:row];
	}
	
}

@end
