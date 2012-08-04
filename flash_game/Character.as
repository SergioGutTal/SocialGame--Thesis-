package
{
	import flash.display.MovieClip;
	
	public class Character extends MovieClip
	{
		//*******************
		// Constants:
		
		static public const DEFAULT:String = "default";
		static public const EAT:String = "eat";
		static public const PAUSE:String = "pause";
		
		//*******************
		// Constructor:
		
		public function Character()
		{
			super();
		}
		
		//*******************
		// Methods:
		
		public function showState( label:String, play:Boolean):void
		{ 
			// Pause the current state...
			if( label == Character.PAUSE ){
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
		
		public function eat():void
		{
			showState(Character.EAT, true);
		}
	}
}