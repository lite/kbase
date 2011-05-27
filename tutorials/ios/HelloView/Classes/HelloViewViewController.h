//
//  HelloViewViewController.h
//  HelloView
//
//  Created by dennisli on 1/18/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HelloViewViewController : UIViewController {
	IBOutlet UILabel *decisionText;
}

@property(retain, nonatomic) UILabel *decisionText;


- (IBAction)buttonPressed:(id)sender;

@end

