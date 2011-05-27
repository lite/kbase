//
//  InstatwitViewController.h
//  Instatwit
//
//  Created by dennisli on 1/18/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface InstatwitViewController : UIViewController 
<UIPickerViewDataSource, UIPickerViewDelegate>
{
	IBOutlet UIPickerView *tweetPicker;
	NSArray *activities;
	NSArray *feelings;
}
@property(retain, nonatomic) UIPickerView *tweetPicker;

- (IBAction)sendButtonTapped:(id)sender;

// datasource
- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView;
- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component;

// delegate
- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component;
- (NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component;

@end

