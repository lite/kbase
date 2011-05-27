//
//  IpadTestAppDelegate.h
//  IpadTest
//
//  Created by dennisli on 3/22/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class IpadTestViewController;

@interface IpadTestAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet IpadTestViewController *viewController;

@end
