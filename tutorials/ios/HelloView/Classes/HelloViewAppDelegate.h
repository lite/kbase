//
//  HelloViewAppDelegate.h
//  HelloView
//
//  Created by dennisli on 1/18/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class HelloViewViewController;

@interface HelloViewAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    HelloViewViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet HelloViewViewController *viewController;

@end

