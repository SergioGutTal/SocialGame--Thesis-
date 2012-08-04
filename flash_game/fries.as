package
{
	import flash.display.MovieClip;
	
	public class fries extends MovieClip
	{
		//*******************
		// Variables:
		var power:Number = 0.8;
		var friction:Number = 0.95;
		var gravity:Number = 1;
		var yspeed:Number = 0;
		var xspeed:Number = 0;
		var wind:Number = 1.7
		

		//*******************
		// Constructor:
		
		public function fries()
		{
			super();
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