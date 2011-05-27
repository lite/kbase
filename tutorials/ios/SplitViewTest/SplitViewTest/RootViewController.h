//
//  RootViewController.h
//  SplitViewTest
//
//  Created by dennisli on 3/22/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class DetailViewController;

@interface RootViewController : UITableViewController {
    NSArray* attractions;
}

		
@property (nonatomic, retain) IBOutlet DetailViewController *detailViewController;

@end
