//
//  InstatwitAppDelegate.h
//  Instatwit
//
//  Created by dennisli on 1/18/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class InstatwitViewController;

@interface InstatwitAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    InstatwitViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet InstatwitViewController *viewController;

@end

