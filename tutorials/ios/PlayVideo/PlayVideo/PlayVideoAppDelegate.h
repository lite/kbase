//
//  PlayVideoAppDelegate.h
//  PlayVideo
//
//  Created by dennisli on 3/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class PlayVideoViewController;

@interface PlayVideoAppDelegate : NSObject <UIApplicationDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet PlayVideoViewController *viewController;

@end
