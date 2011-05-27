//
//  InstrusiveViewController.h
//  ModalDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol InstrusiveViewControllerDelegate

- (void) doneButtonPressed:(NSArray* )values;

@end

@interface InstrusiveViewController : UIViewController {

}

@property(nonatomic, retain) IBOutlet UITextField *name;
@property(nonatomic, retain) IBOutlet UITextField *email;
@property(nonatomic, retain) IBOutlet UITextField *password;

@property(nonatomic, retain) id<InstrusiveViewControllerDelegate> delegate;

@end
