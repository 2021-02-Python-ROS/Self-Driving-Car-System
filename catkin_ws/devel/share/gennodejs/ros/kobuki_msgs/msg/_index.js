
"use strict";

let BumperEvent = require('./BumperEvent.js');
let ButtonEvent = require('./ButtonEvent.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let MotorPower = require('./MotorPower.js');
let KeyboardInput = require('./KeyboardInput.js');
let ScanAngle = require('./ScanAngle.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let ExternalPower = require('./ExternalPower.js');
let Sound = require('./Sound.js');
let Led = require('./Led.js');
let CliffEvent = require('./CliffEvent.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let VersionInfo = require('./VersionInfo.js');
let DigitalOutput = require('./DigitalOutput.js');
let ControllerInfo = require('./ControllerInfo.js');
let SensorState = require('./SensorState.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let DockInfraRed = require('./DockInfraRed.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');
let AutoDockingResult = require('./AutoDockingResult.js');

module.exports = {
  BumperEvent: BumperEvent,
  ButtonEvent: ButtonEvent,
  DigitalInputEvent: DigitalInputEvent,
  MotorPower: MotorPower,
  KeyboardInput: KeyboardInput,
  ScanAngle: ScanAngle,
  WheelDropEvent: WheelDropEvent,
  ExternalPower: ExternalPower,
  Sound: Sound,
  Led: Led,
  CliffEvent: CliffEvent,
  RobotStateEvent: RobotStateEvent,
  VersionInfo: VersionInfo,
  DigitalOutput: DigitalOutput,
  ControllerInfo: ControllerInfo,
  SensorState: SensorState,
  PowerSystemEvent: PowerSystemEvent,
  DockInfraRed: DockInfraRed,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingAction: AutoDockingAction,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingFeedback: AutoDockingFeedback,
  AutoDockingResult: AutoDockingResult,
};
