//
//  ModalDemoViewController.h
//  ModalDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

#import "InstrusiveViewController.h"

@interface ModalDemoViewController : UIViewController<InstrusiveViewControllerDelegate> {
    
}

- (IBAction) buttonTapped:(id)sender;

- (void) doneButtonPressed:(NSArray *)values ;

@end
