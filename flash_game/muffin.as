package
{
	import flash.display.MovieClip;
	
	public class muffin extends MovieClip
	{
		//*******************
		// Variables:
		var power:Number = 0.8;
		var friction:Number = 0.95;
		var gravity:Number = 1;
		var yspeed:Number = -20;
		var xspeed:Number = 0;
		var wind:Number = 1.7
		
		//*******************
		// Constants:
		
		static public const DEFAULT:String = "default";
		static public const FALL:String = "muffin_fall";
		static public const PAUSE:String = "pause";
		
		//*******************
		// Constructor:
		
		public function muffin()
		{
			super();
		}
		
		//*******************
		// Methods:
		
		public function showState( label:String, play:Boolean):void
		{ 
			// Pause the current state...
			if( label == muffin.PAUSE ){
				return;
			}
			if( play ){
				gotoAndPlay(label);
			}else{
				gotoAndStop(label);
			}
		}
		
		//---------------
		// shortcuts
		
		public function fall_animation():void
		{
			showState(muffin.FALL, true);
		}
		
		public function fall():void
		{
			xspeed += wind*((Math.random()*3)-1.5);
			yspeed += gravity;
			this.x += xspeed;
			this.y += yspeed;	
			//this.rotation += 0.4*((Math.random()*2)-1);
		}
		
	}
}