//
//  PopoverDemoAppDelegate.h
//  PopoverDemo
//
//  Created by dennisli on 3/23/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class PopoverDemoViewController;

@interface PopoverDemoAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet PopoverDemoViewController *viewController;

@end
