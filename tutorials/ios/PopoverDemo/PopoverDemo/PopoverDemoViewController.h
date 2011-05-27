//
//  PopoverDemoViewController.h
//  PopoverDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

#import "FontChooserViewController.h"

@interface PopoverDemoViewController : UIViewController <FontChooserDelegate> {
    
}

@property(nonatomic, retain) IBOutlet UITextView *allText;
@property(nonatomic, retain) UIPopoverController *popOver;

- (IBAction) buttonTapped:(id) sender;
- (void) fontSelected:(NSString *)fontName;

@end
