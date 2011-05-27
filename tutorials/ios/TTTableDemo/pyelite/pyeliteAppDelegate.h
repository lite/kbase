//
//  pyeliteAppDelegate.h
//  pyelite
//
//  Created by dennisli on 3/28/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class pyeliteViewController;

@interface pyeliteAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet pyeliteViewController *viewController;

@end
