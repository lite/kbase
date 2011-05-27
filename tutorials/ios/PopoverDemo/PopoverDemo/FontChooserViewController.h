//
//  FontChooserViewController.h
//  PopoverDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol FontChooserDelegate

- (void) fontSelected:(NSString*) fontName;

@end

@interface FontChooserViewController : UIViewController {
    
}

- (IBAction) buttonTapped:(id) sender;

@property(nonatomic, retain) id<FontChooserDelegate> delegate;

@end
