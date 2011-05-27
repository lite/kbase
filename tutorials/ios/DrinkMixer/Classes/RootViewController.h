//
//  RootViewController.h
//  DrinkMixer
//
//  Created by dennisli on 2/27/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface RootViewController : UITableViewController {
	NSMutableArray* drinks;
}

@property (nonatomic, retain) NSMutableArray* drinks;

@end
