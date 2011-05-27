//
//  PlayVideoViewController.h
//  PlayVideo
//
//  Created by dennisli on 3/24/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MediaPlayer/MediaPlayer.h>

@interface PlayVideoViewController : UIViewController {
    MPMoviePlayerViewController* player;
}

- (IBAction) buttonTapped:(id) sender;

@end
