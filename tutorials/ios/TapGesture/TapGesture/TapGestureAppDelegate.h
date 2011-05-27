//
//  TapGestureAppDelegate.h
//  TapGesture
//
//  Created by dennisli on 3/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class TapGestureViewController;

@interface TapGestureAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet TapGestureViewController *viewController;

@end
